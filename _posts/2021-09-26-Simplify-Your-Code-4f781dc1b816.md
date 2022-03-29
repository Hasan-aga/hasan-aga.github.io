---
title: Simplify Your Code
description: Clean up nested if-statements with ease.
date: '2021-09-26T09:52:42.187Z'
categories: []
keywords: []
slug: /@hasan-alsulaiman/simplify-your-code-4f781dc1b816
comments: true
---

Clean up nested if-statements with ease.

![](/assets/0__eNSXLy3p1aCNWJh9.jpg)
)
[Cyclomatic complexity](https://www.ibm.com/docs/en/raa/6.1?topic=metrics-cyclomatic-complexity) is defined as the number of **linearly independent paths** through the code, so you are increasing the complexity of your code every time you add an if-statement!

In this post, I show you a simple example of improving code by abstracting nested if-statements.

_Note: there are probably far better ways of doing the following, but I went with the simplest way I could think of._

### The Ugly Code

I was reading about an algorithm that converts numbers to their English names (110 -> one hundred and ten), [the book](https://g.co/kgs/PNHgrg) gave me a code snippet made up of an unreadable nested if statements:

![](/assets/0__njHbS4p4ZVb58zIb.jpg)
)
Can you understand what the code is doing? it took me a while but it is simply formatting the hundreds part of the code then it moves to formatting the tens and ones, the details are irrelevant (get the entire code on [my Github](https://github.com/Hasan-Alsulaiman/implementations/tree/main/src/main/java/ch23_generating_english_words_for_numbers)).

### The Good Code

How to improve the above code snippet? I used two things:

1.  ternary if statement
2.  moving related parts of code to their own methods

and the result:

![](/assets/0__pZ__2aoXFn92GO3Dg.jpg)
)
In my humble opinion; this code is far easier to understand because instead of if statements we get **meaningful function names**.
