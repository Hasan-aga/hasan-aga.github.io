---
layout: post
title: My notes on some articles
date: 2024-02-10
category: [programming]
---

<img src="/assets/2024-02-10-my-notes-on-some-articles/notes.jpg" alt="notes.jpg"/>

In this post I will share some articles that I have read along with some notes from these articles.

## React Query as a State Manager

This articles is written by the creator of the React-query library which is a library for managing remote async state in React project.

[link to article](https://tkdodo.eu/blog/react-query-as-a-state-manager)
React Query is great at managing async state globally in your app, if you let it. Only turn off the refetch flags if you know that make sense for your use-case, and resist the urge to sync server data to a different state manager. Usually, customizing staleTime is all you need to get a great ux while also being in control of how often background updates happen.

React Query will try to keep cache data up to date by refetching at some interval.

once data is fetched, subsequent use of data comes from cache.

BUT if two components render at the same time then react query will do two network calls instead of one since it does not have time.

the article discusses a fix for this which is to change the stale time and lazy load components.

## The const deception

[link to article](https://www.joshwcomeau.com/javascript/the-const-deception/)
This article is written by one of the most talented web developers I know and it is about the `const` keyword in JavaScript.

we must understand the distinction between assignment and mutation.

<img src="/assets/2024-02-10-my-notes-on-some-articles/const.png" alt="const.jpg"/>

assignment is linking some data to a variable, mutation is changing the data itself.

`const` simply means there will be no further assignment, the data itself can still be changed (if it is not immutable)

but we still can change (mutate) the array itself: `fruits.push("whatever")`

<aside>
💡 There's a fundamental distinction between re-assignment (pointing a variable name at a new thing) and mutation (editing the data within the thing).
When we create a constant with const, we can be 100% sure that the variable will never be re-assigned, but no promises are made when it comes to mutation. const doesn't block mutation at all.

</aside>

### freezing objects and arrays

to guarantee that our data won't be edited, we can use `Object.freeze`

```jsx
// With arrays:
const arr = Object.freeze([1, 2, 3]);
arr.push(4);
console.log(arr);
// -> [1, 2, 3]
// With objects:
const person = Object.freeze({ name: "Hassan" });
person.name = "Sujata";
console.log(person);
// -> { name: 'Hassan' }
```

Also, if you use TypeScript, you can use the as const

```jsx
const arr = [1, 2, 3] as const;
arr.push(4);
// 🛑 Error: Property 'push' does not exist
//           on type 'readonly [1, 2, 3]'.
```

### primitive data types

all primitive data types in JavaScript are *immutable.*

we think about it using this example, if this code were to pass then the number 36 would be deleted and **could never be referenced again!**

# queuing a series of state updates

[Queueing a Series of State Updates – React](https://react.dev/learn/queueing-a-series-of-state-updates)

sometime we want to set a state and use it immediately in an api call. I have a list of buttons on the screen and when one of them is clicked I want it to become active visibly and I also want to take its value and send it to the backend via api call.

in react our first instict is to use a state to store the active value and use it in the api call.

example

```bash
[someState, setSomeState] = useState()

const handleSeriesStartOk = () => {
       callApi(someState])
    };
return (
        <button onClick={handleSeriesStartOk}>
					click me
        </button>
      );
```

the problem in the above code is, when we click a button the setState will not take effect immediately! instead it works in async mode and it waits for all event handlers in your code to return. this is how react is designed to batch the updates and improve performance.

> **React waits until _all_ code in the event handlers has run before processing your state updates.**

> This might remind you of a waiter taking an order at the restaurant. A waiter doesn’t run to the kitchen at the mention of your first dish! Instead, they let you finish your order, let you make changes to it, and even take orders from other people at the table.

this also means that when you make the api call immediately on click, you may endup sending the wrong data.

### the problem with our code

we use the state in functions that make api calls but these api calls need to be triggered by useEffect instead:

### solution

use useEffect to make api calls

# 6 pivotal moments in open source history

[6 pivotal moments in open source history](https://opensource.com/article/18/2/pivotal-moments-history-open-source)

## RMS and the printer

In the late 1970s, Richard M. Stallman (RMS) was a staff programmer at MIT. His department, like those at many universities at the time, shared a PDP-10 computer and a single printer. One problem they encountered was that paper would regularly jam in the printer, causing a string of print jobs to pile up in a queue until someone fixed the jam. To get around this problem, the MIT staff came up with a nice social hack: They wrote code for the printer driver so that when it jammed, a message would be sent to everyone who was currently waiting for a print job: "The printer is jammed, please fix it." This way, it was never stuck for long.

In 1980, the lab accepted a donation of a brand-new laser printer. When Stallman asked for the source code for the printer driver, however, so he could reimplement the social hack to have the system notify users on a paper jam, he was told that this was proprietary information. He heard of a researcher in a different university who had the source code for a research project, and when the opportunity arose, he asked this colleague to share it—and was shocked when they refused. They had signed an NDA, which Stallman took as a betrayal of the hacker culture.

The late '70s and early '80s represented an era where software, which had traditionally been given away with the hardware in source code form, was seen to be valuable. Increasingly, MIT researchers were starting software companies, and selling licenses to the software was key to their business models. NDAs and proprietary software licenses became the norms, and the best programmers were hired from universities like MIT to work on private development projects where they could no longer share or collaborate.

As a reaction to this, Stallman resolved that he would create a complete operating system that would not deprive users of the freedom to understand how it worked, and would allow them to make changes if they wished. It was the birth of the free software movement.
