---
title: Elegantly Log Elapsed Time in Java
description: Avoid repeating your code
date: '2021-09-02T09:43:49.344Z'
categories: [java]
keywords: [learn, debug, programming]
slug: /@hasan-alsulaiman/elegantly-log-elapsed-time-in-java-aa6f91938344
comments: true
---

Avoid repeating your code

![](/assets/0__pVp01gELCM6dsa1__.jpg)
)
Have you ever needed to compare the performance of two methods? the easiest way is to log the execution time of each method, you probably end up with something like this:

{% gist a73c8cfaa798736636dea84c4ee08fc5 smallLog.java %}

but if you wanted to compare more than two methods the process gets ugly as you end up repeating yourself:

{% gist a73c8cfaa798736636dea84c4ee08fc5 uglyLog.java %}

in this article I will explain a better way.

#### Don’t repeat yourself

it would be better if we can write a method that **takes as argument another method** and runs that method inside the time logging code (such as the one above), well, it turns out we can write such a method using **_Java functional interface_** and **_method referencing_**, but what are those things?

#### Java Functional Interface

A _functional interface_ is an interface that contains **one and only one** abstract method.

{% gist a73c8cfaa798736636dea84c4ee08fc5 functionalIF.java %}

because it has only one method, it means we can implement this interface using a lambda, or we can use method referencing.

#### Java Method Referencing

As the name suggests, method referencing is the process of passing a reference of a method to be stored in a variable, for the above interface, the type of the variable will be _MyFunctional_ and here is how we do it:

{% gist a73c8cfaa798736636dea84c4ee08fc5 method$Func.java %}

first we create a **static** method that matches the signature of the abstract method in our interface

and then we put the reference in a variable as follows:

{% gist a73c8cfaa798736636dea84c4ee08fc5 methodRef.java %}

similarly, we can pass a method reference to a method that accepts an argument of type _MyFunctional_

{% gist a73c8cfaa798736636dea84c4ee08fc5 logtime.java %}

and we can call the above method as follows:

{% gist a73c8cfaa798736636dea84c4ee08fc5 logtimeDemo.java %}

#### Putting it all together

what’s left is to add time logging to our _logTime_ method, and it ends up like this:

{% gist a73c8cfaa798736636dea84c4ee08fc5 allTogether.java %}

#### Small Improvements

The above code uses a functional interface that we created manually, it turns out that Java has built-in functional interfaces that we can use to speed things up,

in this case we will use **_BiFunction<T,U,R>_** since it fits _myAdd’s_ signature (it accepts two arguments and returns result), you can look up the [list of functional interfaces](https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html) which fit most common method signatures.

using **_BiFunction<T,U,R>_** our code will look like this:

{% gist a73c8cfaa798736636dea84c4ee08fc5 biFunc.java %}

so now, every time we want to log a method that accepts two Integer arguments and returns an Integer result we can simply pass it to the _log_ method above as follows

{% gist a73c8cfaa798736636dea84c4ee08fc5 notUgly.java %}

#### Extra note

in Python, we would do the same thing except we would use **_Decorators_** instead, and since functions are 1st class citizens we would end up with a much more usable scheme.
