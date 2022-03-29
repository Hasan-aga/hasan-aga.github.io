---
layout: post
title: "Five Reasons to Love FISH"
categories: Linux
---

A beautiful, well-built alternative to BASH, here is why you should try it.

![clear drinking glass on brown wooden table](https://images.unsplash.com/photo-1613987108430-b4bb3863e595?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=Mnw5MDg0MHwwfDF8c2VhcmNofDF8fHR1cmtpc2glMjB0ZWF8ZW58MHx8fHwxNjQ4NTU0ODc3&ixlib=rb-1.2.1&q=80&w=1080 "Olga Pukhalskaya")

# What is FISH?

FISH stands for **F**riendly **I**nteractive **Sh**ell. It simplifies many of the common tasks that we perform using shells such as running commands, creating *aliasis* or *environment-variables*. 

# Reasons to Love FISH

## 1. Auto-completion

When you type a command into the terminal, FISH searches your history and predicts the command as you are typing! 

![auto-complete-command.gif](/assets/auto-complete-command.gif)

FISH also looks at the current directory and predicts the valid file and directory names as you type them.

![auto-complete.gif](/assets/auto-complete.gif)

To accept the autosuggestion press `→`. To accept the first suggested word, press `Alt+→`. If the autosuggestion is not what you want, just ignore it: it won't execute unless you accept it.

## 2. Syntax Highlighting

FISH interprets the command line as it is typed and highlights potential errors such as non-existing commands. It also highlights parentheses or quotes

![syntax-parenthesis.gif](/assets/syntax-parenthesis.gif)

## 3. Easy configuration

FISH uses a web-based configuration. you type `` fish_config`` and it opens a configuration web page in your browser

![webconfig.png](/assets/webconfig.png)

FISH also has a package manager [Oh-my-fish](https://github.com/oh-my-fish/oh-my-fish) that helps you install plugins and themes.

## 4. Themes and Customization

Themes can change the look of FISH in many ways, from the syntax highlighting to the prompt style. there are many [themes](https://github.com/oh-my-fish/oh-my-fish) that you can pick from.

<img title="" src="/assets/theme2.png" alt="theme2.png" data-align="center">

<img title="" src="/assets/theme1.png" alt="theme1.png" data-align="center">

## 5. Ease of Use

In BASH, if you want to create an alias you need to open `.bashrc` and define your alias in it then you must source it. In FISH, you simply type ``alias openWithNaut "nautilus ."`` .

If you want to add a path to your $PATH, you can also do it directly from the command-line by using the built-in ``fish_add_path [paths...]`` or attaching a new path to the PATH variable.

# Final thoughts

The above mentioned features are merely what I like the most, there are more features that I have used and found useful but in order to keep this short I did not add them. If you want to take a look at FISH then headout to their [site](https://fishshell.com/) where they have excellent tutorials to help you get started.
