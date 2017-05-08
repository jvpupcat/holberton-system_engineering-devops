# Shell, init files, variables, and expansions

<img src="https://www.trubahamianfoodtours.com/wp-content/uploads/2014/05/queen-conch-endangered-list_0.jpg">

## Description

Sh is the Bourne shell (sh). It is the oldest and widely used shell that was written by Steven
Bourne. There are newer variations of the shell program such as the C shell (csh), Korn shell (ksh),
Bourne again shell (bash).

* C shell was written by Bill Joy.
* Korn shell was written by David Korn.
* Bourne again shell was written by primary authors, Brian Fox and Chet Ramey.

While there are different shell variations, they work similarly. Well-built shells are designed
for interactive and interpretation use. Shell scripts are text files containing shell commands that
need interpreting before the shell can execute a command. Each of the shells listed above have the
facilities associated with programming language: variables, loop and conditional statements, I/O
commands, and functions.

Because each shell is different, there will be differences with variations and syntax.

### Special Parameters Used

* ``$`` - used for expansions.

### Commands Used

* ``echo``,

## Brief Synopsis

Every file in this repo is an executable script. The file will start with the following:

* ``#!/bin/bash``

To make a file executable, the chmod command was used. To use the files listed in this repo, please
use ``git clone`` to clone the scripts into your terminal.

## What Each Script Does

* ``0-alias`` - assigns 'rm * ' to an preexisting command, ls.
* ``1-hello_you`` - greets a user by their username.
