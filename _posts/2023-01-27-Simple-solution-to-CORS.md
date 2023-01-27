---
layout: post
title: "Simple Solution to CORS"
date: 2023-01-27
categories: [programming, web]
comments: true
---

CORS is a security rule that applies to browsers. It prevents a page from accessing a server if they sit on different domains. A hacker could otherwise access your bank account from a malicious page.

It is also a pain in the back for developers like me. Last week I wanted to call and RSS feed endpoint from a React app that I am building and got stopped by CORS. Here is how I solved the problem:

## CORS Only works on browsers
Since this rule only applies to browsers. A simple solution is to make your API call from the backend not the frontend. That way the call is not being made from a browser and should work.

A quick way to get a backend is to use a serverless function such as the ones offered by Azure or AWS.

You would write a function that simply calls an API and returns the results then you simply call this function from you frontend.