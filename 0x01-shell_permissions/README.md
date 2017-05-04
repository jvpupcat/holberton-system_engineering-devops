# Shell, permissions

<img src="https://www.devsaran.com/sites/default/files/styles/large/public/blogimages/badges_dd_console_stage2.png?itok=9iOE8EyD">

## Description

The operating systems in Unix aren't just multitasking systems. They're also multi-user systems. 
Because of that, it's necessary to set permissions for owner, group owner, or the public or 
everyone. In the Unix security model, a user may own files and directories. By owning a file or
directory, the user has control over access. Users can also belong to a group.

Every file and directory are given permission using ``chmod``. To change permissions, use the following:

* example: ``chmod ugo+x filename``

In the example above, I am granting execution rights to filename. Every file and directory has read, 
write, or execute permissions and it is entirely up to the creator of the files/directories to decide
who gets what permissions. 

### Commands Used

* ``mkdir``, ``chmod``, ``id``, ``sudo``, ``su``, ``chown``, ``chgrp``, ``groups``, ``whoami``,
``adduser``, ``useradd``, ``addgroup`` 

## Brief Synopsis

Every file in this repo is an executable script. The file will start with the following:

* ``#!/bin/bash``

To make a file executable, the chmod command was used.

## What Each Script Does

* ````
