---
layout: post
title: Clearing ASP.NET control values
categories:
  - asp.net
---
Have you ever needed to clear the values of a bunch of TextBoxes on your ASP.NET page?
Not all the TextBoxes, but maybe all the ones in a certain Panel. Or maybe you need
to reset all the DropDownLists too?

This is a method I wrote to do just that. It clears the values of all child
controls under a given parent. Enjoy.

<script src="http://gist.github.com/201768.js"></script>