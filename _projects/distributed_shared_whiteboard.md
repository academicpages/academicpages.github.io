---
title: "✏️ Distributed Shared Whiteboard"
collection: projects
permalink: /project/distributed_shared_whiteboard
excerpt: 'A shared whiteboard desktop application that allows multiple users to draw shapes and chat at the same time.'
date: 2019-10-01
---


<div>
  <img src="/images/distributed_shared_whiteboard/welcome.png" alt="dsw_welcome"> 
</div>

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [Project Timeline](#project-timeline)
- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Usage](#usage)
  - [Step 1](#step-1)
  - [Step 2](#step-2)
  - [Step 3](#step-3)
  - [Step 4](#step-4)
  - [Step 5](#step-5)
- [Demo](#demo)
  - [Whiteboard Server GUI](#whiteboard-server-gui)
  - [Client GUI](#client-gui)

<!-- TOC end -->

# Project Timeline

August 2019 - October 2019

> **Github: [https://github.com/ZhangzihanGit/Distributed-Shared-Whiteboard-Application](https://github.com/ZhangzihanGit/Distributed-Shared-Whiteboard-Application){:target="_blank"}{:target="_blank"}**

# Project Description

A shared whiteboard desktop application that allows multiple users to draw shapes and chat at the same time. Users need to log in/sign up to join a whiteboard session, all passwords are encrypted using the `SHA512` algorithm. Multiple whiteboards could be created, and the user is able to choose whatever whiteboard to join.

The project used Java 8 as the backend language, JavaFX as the frontend framework, and used a three-tier Client/Server architecture. It separated the client – whiteboard server – data server. Java RMI was used as the communication method between the whiteboard server and data server, the request sends from the client were remotely called in the whiteboard server as well. To synchronize each client, MQTT was used to provide a subscribe/publish protocol. The whiteboard server was used as an intermediate agent to accept messages from each client and publish the messages to all other subscribers.

# Tech Stack

- **Backend**: Java
- **Frontend GUI**: JavaFX
- **Communication protocol**:
- **Java RMI**: all communication between whiteboard server and data server, clients send request to whiteboard server
- **MQTT**: whiteboard server publish updates to all subscribed clients
- **Access control**: manager has all the rights to create/delete/close a whiteboard session, as well as save shaps and import files. The manager also has the right to manage the access of visitors

# Usage

<aside>
⚠️ Prerequisite: JDK 8 installed.
</aside>

## Step 1

`git clone <https://github.com/ZhangzihanGit/Distributed-Shared-Whiteboard-Application.git`

## Step 2

`cd Distributed-Shared-Whiteboard-Application/runnable-jar`

## Step 3

Run the data server:

`java -jar dataServer.jar -ip <network_ipv4_address> -p <port_number>`

Example:

`java -jar dataServer.jar -ip localhost -p 1111`

## Step 4

Run the whiteboard server:

`java -jar wbServer.jar -ip <network_ipv4_address>`

Example:

`java -jar wbServer.jar -ip localhost`

## Step 5

Run the client application:

`java -jar client.jar`


# Demo

## Whiteboard Server GUI

<div>
  <img src="/images/distributed_shared_whiteboard/welcome_server.png" alt="welcome_server"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/configure-db.png" alt="configure-db"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/configure-wb-server-port.png" alt="configure-wb-server-port"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/configure-wb-server-mqtt.png" alt="configure-wb-server-mqtt"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/wb-server-list.png" alt="wb-server-list"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/wb-server-monitor.png" alt="wb-server-monitor"> 
</div>

<br>

## Client GUI

<div>
  <img src="/images/distributed_shared_whiteboard/login.png" alt="login"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/signup.png" alt="signup"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/role.png" alt="role"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/manger-naming-wb.png" alt="manger-naming-wb"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/choose-wb-to-join.png" alt="choose-wb-to-join"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/manger-reponse.png" alt="manger-reponse"> 
</div>

<div>
  <img src="/images/distributed_shared_whiteboard/homepage.png" alt="homepage"> 
</div>