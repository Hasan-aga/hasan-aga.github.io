---
title: Floodlight installation guide
description: a more up-to-date guide on installing the famous SDN controller
date: '2021-12-20T21:15:52.334Z'
categories: []
keywords: []
slug: /@hasan-alsulaiman/floodlight-installation-guide-df3635a2b049
comments: true
---

a more up-to-date guide on installing the famous SDN controller

#### Why Floodlight?!

There are many SDN controllers out there, but some of the reasons why you will want to use Floodlight is that it is open-source and it also has nice startup tutorials.

#### Why not follow the official guide?!

I tried following it and I found that it is somewhat outdated, for example, it recommends using Ant to build the project despite Ant support having been deprecated by the project.

### The Guide

#### Dependencies

We will use Maven, so install it by running this command:

```bash
sudo apt install maven
```

Floodlight needs JDK-8 to run, on Linux you can type:

```bash
mvn -version
```

in the terminal to check if you have the right version, if you do, you should see an output like the following:

```bash
Apache Maven 3.6.3 
Maven home: /usr/share/maven 
Java version: 1.8.0\_292, vendor: Private Build, runtime: /usr/lib/jvm/java-8-openjdk-amd64/jre 
Default locale: en\_US, platform encoding: ISO-8859-1 
OS name: "linux", version: "5.4.0-42-generic", arch: "amd64", family: "unix"
```

if you don’t have JDK-8, you can install it using:

```bash
sudo apt install openjdk-8-jdk-headless

install other dependencies using:

sudo apt-get install build-essential ant python-dev
```

#### Build the project

after downloading the dependencies, go ahead and clone Floodlight and cd into it:

```bash
git clone git://github.com/floodlight/floodlight.git

cd floodlight

git submodule init

git submodule update
```

we use maven to first compile the project and then package it as follows, change directory to floodlight and:

```bash
mvn compile  
mvn package
```

make sure that you change the permissions of the floodlight directory to allow writing.

You should now have a .jar file inside the “Target” directory, you can run it by:

``java -jar target/floodlight.jar``

This will run an instance of Floodlight, but you will probably want to do some development on the code, so, to get a project that you can open in your IDE, cd into the Floodlight directory and run

``ant eclipse``

this will generate a Java project that you can open in Eclipse or IntelliJ, I personally could not get it to work in eclipse but it worked in IntelliJ.

### Final note

I wrote this during some very busy time and it may be missing some steps 🤷🏻‍♂️
