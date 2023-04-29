---
layout: post
title: "How to cache expensive components in React"
date: 2023-04-19
categories: [programming, web]
comments: true
---

A Guide to Cache expensive components in React: Use a simple React hook can cache a component that takes a long time to load, and improve your application's user experience.

<img src="/assets/2023-04-19-using-react-hooks-to-cache-entire-web-pages/react.jpg"/>

## Problem

I was working with a react native component that renders a webview. the webview then makes an API call and fetches a bunch of medical images (dicom images). The problem was that when user switches between the patient’s medical links, it would need to re-fetch the images even if the patient was previously rendered.

## Solution

the solution that I came up with is as follows:

1. get a list of links for all patient’s medical links.
2. render a memoized (pure) webview for each link.
3. hide all webviews except for the one that belongs to the currently selected patient.

## Details

the first step is simple. the second step requires creating a memoized webview. this is important since we do not want the webview to rerender if its parent is rerendered.

But why does React rerender?

I recommend looking at [this post](https://www.joshwcomeau.com/react/why-react-re-renders/) by Josh who is one of the best frontend engineers out there. Long story short: Every re-render in React starts with a state change. It's the only “trigger” in React for a component to re-render.

We can indicate to React that our component does not need to be rerendered when its parent rerenders by utilizing the `useMemo` hook:

```jsx
export default function CachedWebview({ webviewURL }) {
  return useMemo(() => {
    return <WebView source={{ uri: webviewURL }} />;
  }, [webviewURL]);
}
```

Now our component will only be rerendered if `webviewURL` changes.

We render this component for each link that the patient has, but we only display the currently selected link and hide every other webview. but this is the second part of the trick, we do not destroy the other webviews and instead simply make them invisible using css styling.

```jsx
return (
    <>
      {webviewLinks.map((link, index) => {
        return (
          <View
            style={
              isSelectedWebview(link, selectedWebviewLink)
                ? styles.visibleView
                : styles.hiddenView
            }
            key={link + index}>
            <CachedWebview count={count} webviewURL={link} key={link} />
          </View>
        );
      })}
    </>
  );
}

const styles = StyleSheet.create({
  visibleView: {
    flex: 1,
    flexDirection: 'column',
  },
  hiddenView: {
    display: 'none',
    height: 0,
    width: 0,
    backgroundColor: 'red',
  },
});
```

As you can see `isSelectedWebview` switches the styling of the webview. If that webview was not the selected one then we give it a height and width of zero and a `display: 'none'`

Why don’t we just do something like this:

```jsx
isSelectedWebview(link, selectedWebviewLink) ? <CachedWebview /> : "";
```

We do not do this because it would mean that each time the user selects a new webview, we would create a new webview from zero and destroy the previous webview which means we would need to reload the images of previously selected webviews (which takes too long).
