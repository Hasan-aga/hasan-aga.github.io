---
layout: post
title: How java hashmap handles collisions
date: 2024-09-25
category: [programming]
---

<img src="/assets/2024-09-25-how-java-hashmap-handles-collisions/cat.jpg" alt="cat.jpg"/>

We will cover what happens after a `put` operation:

1. No collision.
2. Collision

When a collision occurs, hashmap creates a linked list or tree. the interesting part is how do we retrieve the value of a key that had a collision?

Think about it, this key had a collision with a previous key, so both values had to be saved in a linked list (or tree) but how do we retrieve the value? we must be storing the key-value with each linked list (or tree) element.

## How data is represented in the hashmap

Data is represented as a `Node` inside the hashmap, here is the `Node` class:

```java
static class Node<K,V> implements Map.Entry<K,V> {
        final int hash;
        final K key;
        V value;
        Node<K,V> next;

        Node(int hash, K key, V value, Node<K,V> next) {
            this.hash = hash;
            this.key = key;
            this.value = value;
            this.next = next;
        }

        public final K getKey()        { return key; }
        public final V getValue()      { return value; }
        public final String toString() { return key + "=" + value; }

        public final int hashCode() {
            return Objects.hashCode(key) ^ Objects.hashCode(value);
        }

        public final V setValue(V newValue) {
            V oldValue = value;
            value = newValue;
            return oldValue;
        }

        public final boolean equals(Object o) {
            if (o == this)
                return true;

            return o instanceof Map.Entry<?, ?> e
                    && Objects.equals(key, e.getKey())
                    && Objects.equals(value, e.getValue());
        }
    }
```

This is a basic class with some attributes and getters/setters. The interesting part for me was that we are always storing the key, value and hash. In the case where there is no collision, we don't need the key stored in the node as we can retrieve the value by calculating the hash and using it as an index. But when we do have a collision we will need both the hash and the index.

## Java's hashmap source code

I found the source code [here](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/HashMap.java#L281)

```java
 final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
        Node<K,V>[] tab; Node<K,V> p; int n, i;
        if ((tab = table) == null || (n = tab.length) == 0)
            n = (tab = resize()).length;
        if ((p = tab[i = (n - 1) & hash]) == null)
            tab[i] = newNode(hash, key, value, null);
        else {
            Node<K,V> e; K k;
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            else {
                for (int binCount = 0; ; ++binCount) {
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, value, null);
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)
            resize();
        afterNodeInsertion(evict);
        return null;
    }
```

The above function is the `put` implementation, lets break it down:

1. We get `hash`, `key` and `value` (this is important, we get the hash and the key not just the hash).

2. We define a node array `tab` and a node `p` . we also define two int `n` and `i`.

3. We set `tab` to `table` and initialize it if it is null or has a length of zero 
   ```java
   if ((tab = table) == null || (n = tab.length) == 0)
       n = (tab = resize()).length;
   ```

4. We use the hash to calculate the index `i`, `n` is always the size of the node array. `n-1 & hash` is basically a modulo operation (modulo operation makes sure that the index does not go out of bounds). we use `AND` instead of modulo `%` because it is faster but the end result is the same. if the value at this index is `null` it means we have **no collision** and we simply create a new node:
   ```java
   if ((p = tab[i = (n - 1) & hash]) == null)
       tab[i] = newNode(hash, key, value, null);
   ```

5. Here we handle the **collision case**. what is a collision? if the location into which we are trying to insert the value is already occupied that means we have a collision. there are 3 cases in the collision:

   1. if the key used in the new `put` is equal to the key of the already existing node: in this case we simply replace or overwrite the old value
      ```java
      if (p.hash == hash &&
          ((k = p.key) == key || (key != null && key.equals(k))))
          e = p;
      ```

      this makes sense because doing two `put` operations with the exact key should result in overwriting the value.

   2. If the key of the first node and current key are different and the existing value is a tree (not a linked list):  we insert a new value into the tree

   3. If the key of the first node and current key are different and the existing value is a linked list: we traverse the linked list until we find the end, then we insert a new node into the linked list at the end. we also handle the case where the size of the linked list is larger than a threshold and in that case we convert to tree (tree works better than really large linked lists)
      ```java
      for (int binCount = 0; ; ++binCount) {
          if ((e = p.next) == null) {
              p.next = newNode(hash, key, value, null);
              if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                  treeifyBin(tab, hash);
              break;
          }
      ```

      if before reaching the end of the linked list we find a node that has the same key as the current key then we break the loop.
      ```java
      if (e.hash == hash &&
          ((k = e.key) == key || (key != null && key.equals(k))))
          break;
      ```

      if we reach the end of this iteration and none of the above conditions is met, we move to the next node:

      ```java
          p = e;
      }
      ```

   4. `onlyIfAbsent` is a flag that can be used to disable overwriting the values of existing keys. by default, hashmap will overwrite so `onlyIfAbsent` is `false` 

      ```java
      if (e != null) { // existing mapping for key
          V oldValue = e.value;
          if (!onlyIfAbsent || oldValue == null)
              e.value = value;
          afterNodeAccess(e);
          return oldValue;
      }
      ```

      this is where we update the value of a node that has the same key as the current key, we come here from the above `break`

      also, ` afterNodeAccess(e);` is actually and empty method so it makes no difference!

      ## key take

      what was surprising to me is that in the case of a collision we always store the key of each collided entry. 