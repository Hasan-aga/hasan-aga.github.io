---
layout: post
title: "How I paid the price of over-engineering"
date: 2023-05-15
categories: [web]
comments: true
---

<img src="/assets/0__eNSXLy3p1aCNWJh9.jpg" alt="street signs"/>

TLDR: my blog was hosted in once place and it was fetching its styles from a remote place (github pages can use remote themes). somewhere along the line a request to http was being made. this request gets blocked by web browser as part of the block-mixed-content policy (an https webpage can only request resources from https and not http).

## Solution

The solution was to go to my remote theme repo and replace the line that calls the stylesheets so it uses https intead of http in the link, in my case it was in `/swiss/_includes/head.html` (I am using a theme called swiss)

before:

```
  href="{{ "/assets/style.css" | prepend: full_base_url }}">

```

after:

```
  href="{{ "/assets/style.css" | relative_url }}">

```

The above syntax is that of a remote html templating language called "Liquid" which is used by Jekyll. Jekyll is a static-site engine used by Github pages.

Static sites are those sites that do not fetch data from any backend. Since they do not need to fetch data, we can simply build them in advance and keep them as _static_ files on the server. Static websites are faster to load since we do not need to wait for the backend to populate the content of our website before serving it to the users.

Github pages is a service offered by Github and it only works with static websites.
