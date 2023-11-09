---
layout: post
title: "Checkout a branch without commiting/stashing local changes"
date: 2023-11-09
categories: [Git]
comments: true
---

<img src="/assets/2023-11-09-checkout-any-branch-without-needing-to-commit-or-stash-local-changes/git.jpg" alt="ai-**generated** poster"/>

https://git-scm.com/docs/git-worktree

this command copies the entire repo into a new tree that will appear as a sub dir. then you can explore that shit as you want knowing that the original tree is untouched.

example, I am at branch A and I want to check something at branch master:

```jsx
git worktree add testTree master
cd testTree
```

the result of the above commands will be the creation of a new copy of your repo into a sub directory called testTree where the branch will be master. then we `cd` into that directory,

after finishing our work we can easily delete the sub directory:

```jsx
git worktree remove testTree
```