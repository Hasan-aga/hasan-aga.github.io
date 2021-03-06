---
layout: post
title: "Feature-matching using BRISK"
date: 2020-12-20
categories: python
comments: true
---

an open-source alternative to SIFT

![](/assets/1__mLIMuhr__hhYP18TGGjpMoA.jpeg)

I wanted an app that takes two images and detects the position of the first image in the second, I also didn’t want to use Artificial intelligence.

What I need to do can be summed up in three steps:  
1\. find good keypoints (or features) on the first image  
2\. do the same on the second image  
3\. match the keypoints of the first image to those of the second

Simple enough won’t you say?! lets see our options

For a task this simple I didn’t want to use AI, I just started learning AI and I’m a total noob, the next best thing is an algorithm called SIFT!

#### **SIFT**

scale-invariant feature transform (**SIFT**) is a feature detection algorithm in computer vision to detect and describe local features in images, it was developed by David Lowe in 1999 and both the algorithm and it’s developer are very famous in the field of CV, **But,** it is patented!

#### **BRISK**

BRISK is a feature point detection and description algorithm with scale invariance and rotation invariance, developed in 2011 as a free alternative to SIFT and readily implemented in famous CV libraries such as OpenCV

#### Step one: finding features

to illustrate I will use the following two images:

![](/assets/1__k02cVMqiaUJBVkmrUF58VQ.jpeg)
![](/assets/1__SaRtd0__7M8jmKsyY0GcpzQ.jpeg)

{% gist 125f06fdba38f5f04e745a8f6d7556f6 %}

#### Explanation

we need to compute feature points on both images, these are points the algorithm finds interesting.

detector = cv.BRISK\_create()

```Python
kp1, desc1 = detector.detectAndCompute(img1, None)
```
we initiate a detector object, and use it to compute the features and descriptors of each point, descriptors will help us match the points between the images, here is the results of the first step

![](/assets/1__q8NyLmPimfa0a6FOaTNQ8Q.jpeg)
)
and the same for image 2

![](/assets/1__S9oooywQ3WA1PLxTvKJpOg.jpeg)
)
_note that if you are using large images this may take more time so consider resizing your image._

now to the fun part, we match the two images,
```Python
FLANN_INDEX_LSH    = 6
flann_params= dict(algorithm = FLANN_INDEX_LSH,
table_number = 6, # 12
key_size = 12,     # 20
multi_probe_level = 1) #2
matcher = cv.FlannBasedMatcher(flann_params, {})
raw_matches = matcher.knnMatch(desc1, trainDescriptors = desc2, k = 2)
```
FLANN is a matcher object, it will give us matches that may contain some inaccuracy, to eliminate inaccurate points we use Low’s ratio test, here I’ve made a function for that

{% gist 9d3989402bddfbc4ff432f4fba8fa50a %}

I also want to draw a bounding box around the detected object, I will do this using Homography, simply put, I will project the borders of my first image on its new location in the second image, here is what that looks like


![](/assets/1__mLIMuhr__hhYP18TGGjpMoA.jpeg)

I have made a function to do homography, here is what it looks like:

{% gist 55a60c18766d0d30ba6b05e0110ed493 %}

You can find the entire code [here](https://github.com/Hasan-Alsulaiman/BRISK-matching), most of it is self-explanatory, but if you have a question feel free to ask me.
