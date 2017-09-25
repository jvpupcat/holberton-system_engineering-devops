# Processes and Signals

<img src="https://cdn3-d.bonitasoft.com/sites/default/themes/bonitasoft4/images/product/v2/icon-adapt.png">

## Overview

PID stands for process identification number. The PID is automatically assigned to each process when it is created on a UNIX-like operating system. A process is a running instance of a program and each running instance is guaranteed a unique PID. The only process that has the same PID on any session is known as the PID init. Init is always the first process on the system and is the ancestor of all other processes.

The default maximum value of PIDs is 32,767. The number represents the total number of processes that can exist simultaneously on a system. The total number of processes can change depending on the size of the system or servers. Larger servers may require many more processes. The maximum number of processes on a system is only limited by the amount of physical memory available.

The PIDs for the processes can be found by using the ps command or the pstree command. The pstree command shows the process names and PIDs in a tree diagram. The top command also shows the PIDs of currently running process, but it differs in that it continuously updates the information. The pidof command provides the PID of a program whose name is passed to it as an argument. The PID is needed in order to terminate a frozen or misbehaving program with the kill command. The kill command can end a program that cannot otherwise be stopped except by rebooting the system.

## What you should learn from this project

At the end of this project you are expected to be able to explain, without the help of Google:

* What is a PID
* What is a process
* How to find a process PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

## Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
