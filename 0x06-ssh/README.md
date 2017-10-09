# 0x06-SSH

SSH is a secure protocol used as the primary means of connecting to Linux servers remotely. After connecting, all commands typed in a local terminal are sent to the remote server and executed there.

The most common way of connecting to a remote Linux server is through SSH. SSH stands for Secure Shell and provides a safe and secure way of executing commands, making changes, and configuring services remotely. An example of an SSH is vagrant.

## How it works

SSH is a text-based, interactive interface that allows a user to interact with their server. Any command typed into the local terminal are sent through an encrypted SSH tunnel and executed on the server. The connection is implemented using a client-server model. The client-server model means that the SSH connection is dependent on the remote server that uses a software called SSH daemon. The software is responsible for "listening" for connections on a specific network port, aunthenticates connection requests, and produces the appropriate environment if the user provides the correct credentials.

The user's computer must have an SSH client. That is another piece of softsware that knows how to communicate using the SSH protocol. It can receive information about the remote host to connect to - username and password. The client can also specify details of the connection type they would like to establish.

Clients generally authenticate either using passwords (less secure and not recommended) or SSH keys, which are very secure. SSH keys are a matching set of cryptographic keys which can be used for authentication. Each set contains a public and private key. The public key can be shared freely without concern, while the private key must be vigilantly guarded and never exposed to anyone.

When a client connects to the host, it will inform the server and tell it which public key to use. The server then check it's authorized_keys file for the public key, generate a random string and encrypts it using the public key. The message can only be decrypted by the associated private key.

Upon receipt of this message, the client will decrypt it by using the private key and combine the randomly-generated string. If a match is found, the combination generates an MD5 hash of value and transmit it back to the server.

## Generating and Working with SSH Keys

Generating a new SSH public and private key pair on a local computer is simple enough. Their are a number of cryptographic algorithms that can be used to generate SSH keys - RSA, DSA, and ECDSA.

To generate an RSA key pair, type:
```
Terminal$ ssh-keygen
Terminal$ Generating public/private rsa key pair.
Terminal$ Enter file in which to save the key (/home/demo/.ssh/id_rsa):
Terminal$ Enter passphrase (empty for no passphrase):
Terminal$ Enter same passphrase again:
```

The prompt for `Enter file` allows a user to choose a different place to store their private key. If nothing is typed in, the default is set to whatever is in the parentheses. After that, `Enter passphrase` allows a user to set a password if one is desired as it adds another layer of protection.

## For this assignment:

At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* What is a server
* Where server usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair

### Requirements

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

The advantage of using #!/usr/bin/env bash instead of /bin/bash for instance is that it will make your script portable for different OS where Bash might be in a different location.

