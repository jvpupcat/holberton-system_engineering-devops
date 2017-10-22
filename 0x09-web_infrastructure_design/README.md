# 0x09 Web Infrastructure Design

<img src="https://www.programmableweb.com/sites/default/files/LAMP-stack.jpg">

## Overview

A web infrastructure design is conceptual and is often used to help engineers gain a better understanding of where and when technologies are used. This is especially important when it comes to updating software/hardware that affects how computers are able to communicate with each other. There are several groups that oversee the infrastructure of the internet. Some of the groups include the Internet Society, which provides leadership in addressing issues that impact the future of the internet; ICANN, which coordinates activiities related to the internet's naming system such as IP address allocation and domain name management; and W3C, which is an international community dedicated to developing new protocols and specifications to be used with the web.

So, what exactly does a web infrastructure look like? The image above should give you a simple idea as to how it works. Most web instrastructures are based on a client/server model. The client/server model allows a personal computer such as a laptop or a desktop to communicate and request information from a server, which is another computer whose main job is to serve other computers.

A server provides functionality for other programs or devices. It can serve multiple clients and a single client can use have multiple servers. Some of the services a server provides is directory services, domain name services, proxy server, web server, database services, and etc. In most cases, a server will have a firewall that protects against unwanted software; email service, which allows emails to be received and sent; print serve, which allows users to send print requests to a printer. Some examples of popular web servers is the Microsoft server, which is popular with corporations. Apache 2 is popular amongst websites. Ubuntu's Linux server is also very popular due to it's versatile OS.

The client/server model relies on a number of software and hardware to communicate with one another and have as many as seven layers of communication. In this section, we will cover the most basic client/server model from the starting point to the end point. The starting point starts with the client trying to request information from a website. First, it connects to the internet, then it sends a request via TCP/IP, which are communication protocols that determine how data should travel across the web. Once the request reaches the domain name server, the DNS searches through it's records to see if the unique web address is associated an IP address, a unique identifier. 

Once found, a connection is allowed and established, the client and server communicate using the HTTP language. Often, HTTPs is used which is just a secured Hypertext Transfer Protocol, which means the communication is encrypted and decrypted to keep information safe. This allows files and packets to be transferred. There are two types of component files that a web server hosting a website will send across the internet connection: code files and assets. Code files contain html, css, and javascript. Assets contain multimedia such as images, videos, and music. These files are often sent in multiple small packages to save time.

## Telecommunication Protocols

Telecommunication protocols are exactly what they mean. They are the rules and procedures that software/hardware, client/server follow in order to communicate with each other. Protocols exist on several levels and determine data interchange at the hardware level and application level.

In the Open Systems Interconnection (OSI), there are seven layers that both client and server must observe and abide by. Below is a reference model for how applications can communicate over a network, which I'll briefly go over.

<img src="http://www.infocellar.com/networks/images/OSI-1.png">

At the application stage, communication partners are identified, network capacity is assessed, and communication is opened if network exists.

The presentation stage converts incoming and outgoing data from one presentation format to another. Often, a server will encrypt the information it sends and the client decrypts it upon reception.

The session layer sets up, coordinates, and terminates conversation. This is the layer that is responsible for verifying user authentication. Session is also responsible for timing out a connection if a terminal session is idle for too long and reestablishes connection after an unexpected interruption.

The transport stage manages the packetization of data, the deliver of the packets, and automatically error checks once the packets reach the client.

The network layer handles addressing and routing of the data. It sends data in the right direction and receives incoming transmissions at the packet level. For the internet, IP does this job.

At the data-link stage, it sets up links across the physical network, putting packets into network frames. A frame in telecommunication is data that is transmitted between network points as a unit complete with address and protocol control information. A fram is usually transmitted serial bit by bit and contains a header field. This is where the packets of data are packaged before being sent to the client.

The data-link stage has two sub-layers: Logical Link Control Layer (LCL) and the Media Access Control Layer (MAC). The LCL manages traffic, flow and error control, over the physical medium. It can also identify line protocol and may assign sequence numbers to frames and track acknowledgment. The MAC is concerned with sharing the physical connection to the network among several computers.

Finally, the physical layer conveys bit stream through the network at the electrical, optical, or radio level. It provides the hardware means of sending and receiving data on a carrier network such as Verizon, AT&T, Charter, and etc. Communication like this can use the traditional twisted pair which are copper wires or fiber optic which are cables that rely on light to transmit data.

## TCP/IP

The entire internet protocol suite is a set of rules and procedures that is commonly referred to as TCP/IP. It provides end-to-end communications that identify how data is broken into packets, addressed, transmitted, routed and rescinded at the destination. It is designed to make networks reliable and requires little central management. TCP/IP automatically recovers from failure of any devide on the network. It also uses the client/server model of communication.

It is classified as stateless, meaning each client request is considered new because it is unrelated to previous requests. Being stateless frees up network paths so they can be used continuously.

TCP/IP has 4 layers instead of OSI's seven layers. Those layers are shown below:

<img src="http://www.tcpipguide.com/free/diagrams/tcpiplayers.png">

The application level establishes communication, which means it authenticates users, sets up sessions, encrypts and decrypts data being sent across the internet connection.

The transport level handles end-to-end communication, flow control, multiplexity, and reliability.

The network layer is also known as the internet layer which deals with packets and connects independent network to transport the packets across network connections.

The physical layer only operates on a link. That means it must be hooked up to the ethernet or LAN.

### What you should learn from this project

At the end of this project you are expected to be able to explain, without the help of Google:

* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what are each component doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

### Requirements

* A README.md file, at the root of the folder of the project, is mandatory
* For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
* This project will be manually reviewed:
* As each task is completed, the name of that task will turn green
* Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use imgur but feel free to use anything you want).
* For the following tasks, insert the link from of your screenshot into the answer file
* After pushing your answer file to Github, insert the Github file link into the URL box
* You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
* Focus on what you are being asked:
* Cover what the requirements mention, we will explore details in a later project
* Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
* Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
* In this project, again, avoid going in details if not asked
