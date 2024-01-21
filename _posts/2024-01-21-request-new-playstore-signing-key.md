---
layout: post
title: Request new playstore signing key
date: 2024-01-21
category: [mobile]
---

<img src="/assets/2024-01-21-request-new-playstore-signing-key/android.jpg" alt="android.jpg"/>

Last week, Google prompted me to make updates to my app or risk losing access to my Google Play account! The same account that I paid 25 USD for. 

Anyways, I have no idea where my upload keys were; so I had to create new ones and I wanted to document the process.

# Requesting a new playstore signing key
1. Go to the play developer console.
2. Navigate to Release -> Setup -> App Signing  and then search for "request upload key reset".
3. A new page will appear. The page will contain instructions on generating a new keystore and uploading its certificate. 

### Details on generating new keystore
By running the below command you can generate a new keystore:
```
$ keytool -genkey -v -keystore my-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
```
### more resources
1. [Android: Generate Release/Debug Keystores](https://coderwall.com/p/r09hoq/android-generate-release-debug-keystores)
2. [How To Reset Lost Upload Key on Playstore](https://mobikul.com/how-to-reset-lost-upload-key-on-playstore/)
3. [Play Developer Console](https://play.google.com/console)
