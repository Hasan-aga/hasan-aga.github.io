---
layout: post
title: "How I paid the price of over-engineering"
date: 2023-05-15
categories: [web]
comments: true
---

<img src="/assets/0__eNSXLy3p1aCNWJh9.jpg" alt="street signs"/>

TLDR: While hosting my blog in one place and fetching styles from another place (using GitHub Pages' remote themes), I encountered a problem where a request to an insecure HTTP resource was being blocked by web browsers due to the block-mixed-content policy. This policy restricts HTTPS webpages from requesting resources from insecure HTTP sources.

## Solution

To address this issue, I took the following steps:

Accessed my remote theme repository.
Located the specific line responsible for calling the stylesheets, which was located in `/swiss/_includes/head.html`. (Note: I am using a theme called Swiss.)
Modified the line to use HTTPS instead of HTTP in the stylesheet link.

before:

`href="{{ "/assets/style.css" | prepend: full_base_url }}">`

after:

`href="{{ "/assets/style.css" | relative_url }}">`

The above syntax follows the conventions of "Liquid," a remote HTML templating language utilized by Jekyll. Jekyll, in turn, is a static-site engine employed by GitHub Pages.

Static sites are websites that do not rely on fetching data from a backend. Instead, they are pre-built as static files and served directly to users. This approach offers faster loading times, as there is no need to wait for backend operations to populate the content before delivering it to users.

GitHub Pages, a service provided by GitHub, exclusively supports static websites.
