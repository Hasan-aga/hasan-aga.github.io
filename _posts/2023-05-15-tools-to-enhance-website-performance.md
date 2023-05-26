---
layout: post
title: "Tools to enhance website performance"
date: 2023-05-15
categories: [web]
comments: true
---

A Guide on how to measure and improve the performance of any website using free tools.

<img src="/assets/2023-05-15-tools-to-enhance-website-performance/bear.jpg"/>

## Problem

I was trying out some performance-measuring tools on a website and it showed terrible performance metrics despite the website feeling quick. Here, I will try to write what I learned.

## Solution

To get the most accurate result we must first test the performance in incognito-mode. Web browser apply caching to save resources such as images and fonts between website visits which may give us a wrong impression of our website performance. Incognito mode will call your website as if you are visiting it for the first time.
Here are some of the tools that I used

## Lighthouse from Chrome's devtools

If you right-click and select `inspect-element` you will open a sidemenu, from which you can switch to the "lighthouse" tab and run some performance test. The tests will try to measure the web vitals of your website.
There is also the performance tab. In both cases you can also get recommendation on what to do to improve performance.
<img src="/assets/2023-05-15-tools-to-enhance-website-performance/lighthouse.jpg"/>

## webpagetest.org

[webpagetest.org](https://www.webpagetest.org/)

## pagespeed.web.dev

[pagespeed](https://pagespeed.web.dev/)

## How to improve performance

The usual suspect when it comes to slow website is large images. Compress your images before using them in your website and consider using a modern extension file such as `.webp` instead of `jpeg`. Here is a nice open-source image-compression tool [called squoosh](https://squoosh.app/)

If your site has many images consider lazy-loading them so that they don't all get downloaded on initial startup.

If you use a lot of JavaScript, try to chunkify them (similar to lazy-loading).
