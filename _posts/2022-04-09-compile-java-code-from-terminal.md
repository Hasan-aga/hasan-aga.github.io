---
title: Compile Java Code From the Terminal
description: How to use any terminal to compile and run Java source code.
categories: [java]
keywords: [learn, compile, programming]
comments: true
---



How to use any terminal to compile and run Java source code.

![selective focus photography of man using angle grinder](https://images.unsplash.com/photo-1530191601183-4de2969575ad?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=Mnw5MDg0MHwwfDF8c2VhcmNofDEwfHxsYXRoZXxlbnwwfHx8fDE2NDk0OTk1MTU&ixlib=rb-1.2.1&q=80&w=1080 "Maxime Agnelli")

## What You Need

### Java Source Code

You will need to write your Java code and save it with the `.java` extension.

### Java Compiler

To check if you have one type `javac --version` into the terminal. Also, check that the version of `javac` and that of `java --version` are identical. If not you may get the following error:

```bash
Error: A JNI error has occurred, please check your installation and try again Exception in
 thread "main" java.lang.UnsupportedClassVersionError: MyList has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java
  Runtime only recognizes class file versions up to 52.0
```

Use `sudo update-alternatives --config java` to pick the correct version.

### Steps to Compile and Run the code

1. Open a terminal in the same directory as your `.java` file.

2. Type `javac filename.java`, this will generate `.class` files.

3. Type `java filename` (without extension), this should run your code.
