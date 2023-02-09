---
layout: post
title: "Publishing Your First NPM Package"
date: 2023-02-09
categories: [programming]
comments: true
---
# Publishing Your First NPM Package

This document provides an outline on the steps to take when publishing your first NPM package.

1. Create the package files
2. Create a package.json file
3. Publish the package
4. Maintain the package

![https://images.unsplash.com/photo-1490750967868-88aa4486c946?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb](https://images.unsplash.com/photo-1490750967868-88aa4486c946?ixlib=rb-4.0.3&q=80&fm=jpg&crop=entropy&cs=tinysrgb)

## Create the package files

In your computer, create a new directory and open a terminal.

In the terminal type `npm init` and the tool will ask for information about your new package.

After the operation finishes, you will find a single file named `package.json` inside it is where all the information about your package is kept.

### Adding the actual package

Now you can create a file such as `index.js` and add your code. This works similar to any other project but you must remember to export the functions that you need.

# Publish package

`npm publish` would publish your package but you must first be logged-in to your NPM account via `npm login`.

## Maintain package

What if you want to change the code or maybe update the readme file?

You can only push those updates by doing a version update. This is where you package’s version goes from 1.0.0 to 1.0.1 for example.

Here is how to do it:

After you change you code, use `npm version <update_type>` in the terminal where `update_type` is either patch, major, or minor ([more info](https://docs.npmjs.com/about-semantic-versioning)). Then use `npm publish` to push the changes to NPM.

For example, here is how I might change the readme on an already published package:

1. Do the changes.
2. run `npm version patch` (patch is for small changes)
3. run `npm publish`
