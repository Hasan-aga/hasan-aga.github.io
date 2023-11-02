---
layout: post
title: "Git revert pitfall"
date: 2023-11-02
categories: [web]
comments: true
---

<img src="/assets/2023-11-02-git-revert-pitfall/pitfall.jpg" alt="street signs"/>

create a commit in branch a, then create a new branch b and then revert the commit from a. then merge branch b back into a. what will happen to the commit coming from b?

## **answer**

what happened is that the commit from b did not appear into a when merged and I got 'everything is up to date' when I merged b into a. when i added new changes to the file and created a new commit on branch b then merged into a it created a merge conflict.

## **explanation**

If a commit has been made in branch A and later reverted in branch A, then when you merge branch B (which contains the original commit) into branch A, Git recognizes that the changes introduced by that commit have already been applied and then reverted in branch A. Thus, the state in branch A is considered "more recent" or "more advanced" than the state in branch B regarding that particular change, even though branch B still contains the original commit.

As a result, Git considers the commit already accounted for, and it won't reapply the changes from the original commit in branch B. Instead, you will see the "everything is up to date" message when trying to merge B into A.

## illustrations

create branch b:

```jsx
A:  ---A---B---C---D
                   \
B:                 E
```

revert commit on a:

```jsx
A:  ---A---B---C---D---R
                   \   
B:                 E
```

Merging B into A again: As per your observation, if you try to merge B into A again, Git understands that all the changes from B are already incorporated into A (even if some of them were subsequently reverted). So, you'll get a message that everything is up to date.

## solutions

one solution is to modify the changes on b which will produce merge conflict when merged back into a. 

another solution is to tell git that b is more up-to-date: