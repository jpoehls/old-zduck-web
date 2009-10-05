---
layout: post
title: How to run VBS scripts under different credentials
categories:
  - windows
  - vbscript
---
Today I wrote a VBS script to test out some permission settings on a server.
We were debugging a problem and I needed to find out whether different
user accounts had permissions to see whether a given file existed.

The script was simple enough:

    Dim fso
    Set fso = Server.CreateObject("FileSystemObject")
    MsgBox fso.FileExists("\\superserver\path\to\file.txt")

Now how do I run that script as someone other than the logged in user?
Go to the command line and type:

    runas /profile /user:domain\username "cscript.exe C:\path\to\script.vbs"

When you run that it will prompt for the password of the user account you specified.

Note that if you leave off the `cscript.exe` part you'll get an error about your
VBS file not being a valid Win32 application.

The `/profile` option may not be required depending on what your script is doing...
for my simple script I left it out.

You can check out [this TechNet article](http://www.microsoft.com/technet/scriptcenter/resources/qanda/apr06/hey0428.mspx)
for more details.