---
layout: post
title: "How to sort table in NextUI"
date: 2023-02-19
categories: [programming, nextjs]
comments: true
---

# How to sort table in NextUI

A useful example on how to utilize the sorting functionality that NextUI tables have.

![image](/assets/2023-02-19-how-to-sort-table-in-nextui/jan-antonin-kolar-lRoX0shwjUQ-unsplash.jpg)

## Overview

1. Create a table following any of the [examples](https://nextui.org/docs/components/table) from the NextUI docs.
2. Create a state to hold your data and the `sortDescriptor` object that will be used to help the sorter function.
3. Create a function that will be used to sort your data.
4. Inside the `Table.Body` tag, add the following props: `onSortChange`, `sortDescriptor`

## Details

NextUI tables can be sorted by column. The docs contain one example and it uses `useAsyncList` to load and sort some async data (ex: data coming from network). But what if you are using other tools to manage async data (ex: React Query)? This post is for you.

In my case, React Query was managing the fetching/caching of my data. But it is all the same even if you are using vanilla `useEffect`.

First, we create a state to store our data:

```javascript
const [arr, setArr] = useState({
  items: [],
  sortDescriptor: { direction: "descending", column: "title" },
});
```

The state will have specific type since we want to stay close to the NextUI implementation. Hence we will store the data inside `items` prop and we will have a `sortDescriptor` prop that holds details about the sorting derection and which column are we sorting.

If you are recieving the data from a parent component, then go ahead and place the data inside the `items` array (your data must be an array). If you need to process your data first, you can do that inside a `useEffect` function:

```javascript
useEffect(() => {
  let temp = [];
  for (const [key, value] of Object.entries(data.results)) {
    temp.push(...value);
  }
  setArr({ ...arr, items: [...temp] });
}, [data.results]);
```

Now we create a function to sort our data. This is vanilla js array sorting:

```javascript
function sortArr() {
  const { items, sortDescriptor } = arr;
  items.sort((a, b) => {
    let first = a[sortDescriptor.column];
    let second = b[sortDescriptor.column];
    let cmp = collator.compare(first, second);
    if (sortDescriptor.direction === "descending") {
      cmp *= -1;
    }
    return cmp;
  });
  setArr({
    items,
    sortDescriptor:
      sortDescriptor.direction === "ascending"
        ? { direction: "descending", column: "title" }
        : { direction: "ascending", column: "title" },
  });
}
```

The only addition to the vanilla js array sorting function is using the `sortDescriptor.direction` flag to determine if we should sort ascending or descending. This is useful since we will toggle the direction with each click on the column header (1. click -> sort asc, 2. click -> sort desc).

Finally we create a NextUI table and enable sorting as follows:

```javascript
<Table
  aria-label="Example static collection table with multiple selection"
  css={{
    height: "auto",
    minWidth: "100%",
  }}
  onSortChange={sortArr}
  sortDescriptor={arr.sortDescriptor}
>
  <Table.Header>
    <Table.Column key="title" allowsSorting>
      Title
    </Table.Column>
    <Table.Column>Action</Table.Column>
  </Table.Header>
  <Table.Body>
    {arr.items &&
      arr.items.map((feed, key) => {
        return (
          <Table.Row key={key + 1}>
            <Table.Cell>{feed.title}</Table.Cell>
            <Table.Cell>
              <Button
                onPress={() => mutation.mutate(feed.rowid)}
                css={{ all: "unset", cursor: "pointer" }}
              >
                <Delete />
              </Button>
            </Table.Cell>
          </Table.Row>
        );
      })}
  </Table.Body>
</Table>
```

The important things to note here are: 1. We are rendering `arr.items` inside the `Table.Body` which makes sense since this is where we stored our data. 2. The `Table.Column` has a `key="title"` which is useful to identify the column by which we are sorting. 3. the `Table` has `onSortChange = {sortArr}` which calls our sort array whenever a sortChange event fires. The `Table` also has `sortDescriptor={arr.sortDescriptor}` which passes our `sortDescriptor` which we store in the state. This is important since we toggle this descriptor inside our sort array.

## Final notes

The `onSortChange = {sortArr}` will pass a prop containing an object similar to `sortDescriptor` to out sort function. I have not figured out how best to use this but it is something I wanted to mention.
