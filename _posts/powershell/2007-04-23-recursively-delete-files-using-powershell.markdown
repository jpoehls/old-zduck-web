---
layout: post
title: Recursively delete files using PowerShell
categories:
  - powershell
---
Lately PowerShell has been at the top of my *to learn* stack.
Last week I ordered [PowerShell In Action](http://www.amazon.com/Windows-PowerShell-Action-Bruce-Payette/dp/1932394907/ref=pd_bbs_sr_1/102-7531966-1417704?ie=UTF8&amp;s=books&amp;qid=1177382702&amp;sr=8-1),
it hasn't arrived yet but I've already read about 100 pages out of the PDF I borrowed while I wait on the print.
The book is very well written and describes the core concepts of PowerShell very well.

Having (almost) never written a batch file in my life it is taking a bit for me to wrap my head
around the basics but so far I love it. Compiling C# apps to do simple tasks like iterate
directory structures and process files has always annoyed me. There is just too much
overhead in having to compile and manage both the source code an executable when you
only need the code once (today that is).

I just want to create a script and run it, no compile, no exe - oh,
and since I've been completely spoiled by the .NET Framework I want access
to all of that too. PowerShell fits the bill.

My first task. Find all files with an extension of \*.bak on my C: drive and delete them.

Here was my discovery process...

    #  move to C: drive
    cd c:\

    #  list all files in C:
    dir

    #  list all *.BAK files in C:
    dir *.BAK

    #  do it recursively
    dir -recurse -filter *.BAK

Ok, so now that I've got PowerShell spinning through my entire C: drive
how do I stop it? You can always kill the process but I was in a pretty good
mood today and decided to be nice. This is likely to be one of the most important
things you learn about PowerShell (or rather the command line in general) so remember it well...

    CTRL+C
    
That will halt execution of whatever PowerShell is doing get you back to a prompt.
Very handy for people like me who like tend to hit `[Enter]` before thinking about
how long it might take to run.

It seems you can also press `CTRL+BREAK` to achieve a similar affect.
I'm not sure what the differences are between that and `CTRL+C` right now.

> **TIP:** `dir` (along with `ls`) is just an alias for the `Get-ChildItem` command.
> You can get the full syntax for this command by running `Get-Help dir`.

And if you want to delete all those \*.BAK files you just found?
Just pipe your `dir` command to `del` (which happens to be an alias for `Remove-Item`).

    dir -recurse -filter *.BAK | del