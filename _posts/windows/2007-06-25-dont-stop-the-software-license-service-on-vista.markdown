---
layout: post
title: Don't stop the Software License service
categories:
  - windows
---
Ok. So when [someone refers to you as a guru](http://automaticchainsaw.blogspot.com/),
you feel like you have certain expectations you have to meet. I think I just blew that opportunity. ;)

My Vista workstation at home has been running pretty slow lately, so I figured I'd
see what services I could disable to maybe speed it up. I fired up
Sysinternal's (now Microsoft's) [AutoRuns utility](http://www.microsoft.com/technet/sysinternals/utilities/Autoruns.mspx)
and went to work. I disabled several services and applications, one of them
being a service called "Software Licensing".

The Software Licensing service is described as the following:

> Enables the download, installation and enforcement of
> digital licenses for Windows and Windows applications.
> If the service is disabled, the operating system and licensed
> applications may run in a reduced function mode.

Sounds pretty unnecessary right? Uh, right, that's what I thought...
So after I rebooted my system to admire my new speed boost, I'm greeted
with an error at logon stating that an Error Occurred while Activating Windows.

Obviously I got into safe mode and re-enabled that service but several
things strike me as frustrating here.

1. I activated Windows a long time ago, why does it need a service taking
   up resources just to confirm that fact?
2. When it says "If the service is disabled the operating system
   and licensed applications ***may*** run in a reduced functionmode."
   -- No doubt, they **WILL** function in a reduced function mode...
3. Why did I assume that any services labeled as "Licensing" and published by
   Microsoft would be okay to stop???