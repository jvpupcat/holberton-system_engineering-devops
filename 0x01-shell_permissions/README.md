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

* ``0-iam_betty`` - "su" changes the user ID or becomes superuser.
* ``1-whoami`` - "whoami" prints the effective userid.
* ``2-groups`` - "groups" print the groups a user is in.
* ``3-new_owner`` - "chown" changes the file owner and group.
* ``4-empty`` - "touch" creates an empty file.
* ``5-execute`` - "chmod u+x" changes the execution permissions of a file.
* ``6-multiple_permissions`` - "chmod ug+x" grants execution permissions to multiple users.
* ``7-everybody`` - "chmod a+x" grants execution permissions to everyone.
* ``8-James Bond`` - "chmod 007" grants read/write/execution permissions to other users 
to a particular file using octal.
* ``9-John_Doe`` - "chmod 753" grants rwx to owner, r-x to group owner, -wx to other users to a
particular file.
* ``10-mirror_permissions`` - "chmod --reference=olleh hello" mirrors the permissions of a file.
* ``11-directories_permissions`` - "chmod -R a+x * " grants execution rights to all subdirectories
in current directory to all users.
* ``12-directory_permissions`` - "mkdir -m 751" creates a directory that  grants rwx to owner, r-x
to group owner, and --x to other users.
* ``13-change_group`` - "chgrp" changes the group owner of a particular file.
* ``14-change_owner_and_group`` - "chown -R ownername:groupname * " changes the owner and the group
of all files and directories recursively in the current directory.
* ``15-symbolic_link_permissions`` - "chown -h ownername:groupname" changes the owner of a file with a
symbolic link.
* ``16-if_only`` - "chown --from=specificname desiredname" changes the file to another user only if the
file belongs to a certain person.
* ``100-Star_Wars`` - "telnet towel.blinkenlights.nl" - plays Star Wars episode IV.
* ``101-man_holberton`` - created a man page for holberton school.
