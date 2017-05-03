# Shell, basics


<img src="http://www.hippoquotes.com/img/basic-quotes-tumblr/thumb.jpg">

## Description

This repo has some of the most useful commands that are executable in shell.
The shell is the user-interface between the user and the kernel, which is the
operating system.

### Commands Used

* ``mkdir``, ``ls``, ``cd``, ``less``, ``file``, ``ln``, ``cp``, ``mv``, ``rm``,
``type``, ``which``, ``help``, ``man``, ``pwd``.

## Brief Synopsis

Every file in this repo is an executable script. The file will start with the following:
* ``#!/bin/bash``

To make a file executable, the ``chmod`` command was used.

## What each script does

* ``0-current_working_directory``: ``pwd`` prints the current working directory.
* ``1-listit``: ``ls`` prints a list of directory contents.
* ``2-bring_me_home``: ``cd`` changes the current directory to the home directory.
* ``3-listfiles``: ``ls -l`` lists contents of directory in long format.
* ``4-listmorefiles``: ``ls -la`` lists all contents in long format.
* ``5-listfilesdigitonly``: ``ls -lan`` lists all files in long format with user and group IDs numerically.
* ``6-firstdirectory``: ``mkdir`` creates a specific subdirectory in the ``/tmp`` directory.
* ``7-movethatfile``: ``mv`` moves a file to a subdirectory.
* ``8-firstdelete``: ``rm`` removes a specific file.
* ``9-firstdeletion``: ``rm -r`` removes a specific directory.
* ``10-back``: ``cd -`` changes directory to previous working directory.
* ``11-lists``: ``ls -la . .. /boot`` lists all everything in long format in current, parent, and /boot directory.
* ``12-file_type``: ``file`` displayes file type of a specific file.
* ``13-symbolic_link``: ``ln -s`` creates a symbolic link.
* ``14-copy_html``: ``cp -u`` makes an updated copy a file(s).
* ``15-lets_move``: ``mv [[:upper:]]*`` moves uppercase files to a specific directory.
* ``16-clean_emacs``: ``rm *~`` removes files ending with a tilda (~).
* ``17-tree``: ``mkdir -p`` creates parent directories as needed.
* ``18-commas``: ``ls -amp`` lists everything in the current directory with commas, and slashes if it is a directory.
* ``holberton.mgc``: magic file.
