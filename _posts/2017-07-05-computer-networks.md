---
title: 'Notes for Computer Networks'
date: 2017-07-05
permalink: /posts/2017/07/computer-networks/
<!-- tags:
  - cool posts
  - category1
  - category2 -->
---

# Chapter 1

# Multiplexing
- FDM: the frequency spectrum is divided into frequency bands for individual signals.
    - Wavelength Division Multiplexing is just FDM at very high frequencies
- TDM: the users take turns to use the entire bandwidth for a little burst of time.
- CDMA (Code Division Multiple Access)

# Switching
- circuit switching
    - connection-oriented
    - a complete path established prior to the call, which lasts for the duration
- message switching
- packet switching
    - connection-less
    - data is divided into packets
    - users share network resources (link, router) with store-and-forward approach.
    - route chosen on packet-by-packet basis
    - statistical multiplexing: resource are allocated and shared on demand.
- Virtual circuit:
    - All packets associated with a session follow the same path
    - Route is chosen at start of session
    - Packets are labeled with a VC# designating the route

# Four sources of packet delay
- processing
- queuing
- transmission delay
- propagation delay

# The network core
- mesh of interconnected routers
- how is data transferred through net?
    - circuit switching
    - packet switching

# Network of Networks
- ISP: Internet Service Provider
- Tier-1 ISP
    - can reach every other network on the Internet without purchasing IP transit or paying settlements
    - treat each other as equals
    - national/international coverage (e.g. ChinaGBN, ChinaNet)
- Tier-2 ISP
    - smaller (often) regional ISPs, connect to one or more Tier-1 ISPs, possibly other Tier-2 ISPs
- Tier-3 ISP
    - last hop ("access") network (closest to end systems)
    
# Chapter 2
# Hybrid of client-server and P2P
- Skype
    - voice-over-IP P2P application
    - centralized server: finding address of remote party
    - client-client connection: direct (not through server)
- Instant messaging
    - chatting between two users is P2P
    - centralized service: client presence detection/location
    
# What transport services dies an app need?
- data loss
- delay
- throughput: some apps (e.g., multimedia) require minimum amount of throughput to be “effective”; other apps (“elastic apps”) make use of whatever throughput they get.
- security
![](https://lantaoyu.github.io/files/network-figures/transport-service.png)

# TCP service
- connection-oriented
- reliable transport
- flow control: sender won't overwhelm receiver
- congestion control: throttle sender when network overloaded
- does not provide: timing, minimum throughput guarantees, security

# Identifying processes
process identifier = IP address + port numbers

# Domain Name System
- map between IP addresses and name.
    - www.sjtu.edu.cn --> 202.120.2.119
- **distributed database** implemented in hierarchy of many **name servers**
![](https://lantaoyu.github.io/files/network-figures/hierarchical.png)
    - TLDs (Top-Level Domains)
        - 22+ generic TLDs
        - about 250 country code TLDs
- **application-layer protocol** host, routers, name servers to communicate to resolve names (address/name translation)
- UDP on port 53
- 13 root name services worldwide
    - Contacted by local name server that can not resolve name
        - contacts authoritative name server if name mapping not known
        - gets mapping
        - returns mapping to local name server
- When host makes DNS query, query is sent to its local DNS server
    - acts as proxy, forwards query into hierarchy

# DNS protocol, messages
- DNS protocol: query and reply messages, both with same message format
- identification: 16 bit # for query, reply to query uses same #
![](https://lantaoyu.github.io/files/network-figures/dns.png)

# DNS servers
- Three classes:
    - root DNS servers
    - top-level domain DNS servers: These servers are responsible for top-level domains such as com, org, net, edu, and gov, and all of the country top-level domains such as uk, fr, ca, and jp.
    - authoritative DNS servers
- There is another important type of DNS server called the local DNS server. A local DNS server does not strictly belong to the hierarchy of servers but is nevertheless central to the DNS architecture

# HTTP（HyperText Transfer Protocol）
- Uses TCP
    - client initiates TCP connection (creates socket) to server, port 80
    - server accepts TCP connection from client
    - HTTP messages exchanged between browser (HTTP client) and Web server (HTTP server)
    - TCP connection closed
- HTTP is “stateless”
    - server maintains no information about past client requests
- http request message general format
![](https://lantaoyu.github.io/files/network-figures/http-request.png)
- method types
    - HTTP/1.0
        - GET
        - POST
        - HEAD
    - HTTP/1.1
        - GET, POST, HEAD
        - PUT
        - DELETE

# HTTP response status codes
- Every request gets a response consisting of a status line, and possibly additional information.
- The status line contains a three-digit status code telling whether the request was satisfied, and if not, why not.

# Cookies
- four components:
    - cookie header line of HTTP response message
    - cookie header line in HTTP request message
    - cookie file kept on user’s host, managed by user’s browser
    - back-end database at Web site

# HTTP Performance
- Round Trip Time (RTT): time for a small packet to travel from client to server and back
- Page Load Time (PLT): 
    - One RTT to initiate TCP connection
    - one RTT for HTTP request and first few bytes of HTTP response to return
    - file transmission time
    - total = 2 * RTT + transmission time
    
# Electronic Mail
- mail servers
    - mailbox: contains incoming messages for users
    - message queue: contains outgoing messages to be sent
    - SMTP protocol: between mail servers to send emails messages
        - duplex TCP connection at port 25
        - client: sending mail server
        - server: receiving mail server
- mail access protocol
![](https://lantaoyu.github.io/files/network-figures/mail-access.png)
    - POP:
        - download and delete
        - stateless across sessions
    - IMAP:
        - keep all messages at server
        - keeps user state across sessions
    - http: gmail etc

# CDN: Content delivery network
- Replicate Web pages on a bunch of servers
- Efficient distribution of popular content
- Faster delivery for clients

# MIME
- Multipurpose Internet Mail Extensions
- MIME: to continue to use the RFC 822 format, but to add structure to the message body and define encoding rules for non-ASCII messages.

# P2P
- Distributed Hash Table
    - The distributed index Database has (key, value) pairs;
        - key: content keywords
        - value: IP address of the hosts with the content
    - Assign integer identifier to each peer:
        - ID(peer) = hash(IP, port)
        - each peer only aware of immediate successor clockwise
    - How to store (key, value) pairs in peers?
        - Rule: store (key, value) pair to the peer that has the closestID.
        - Convention: closest is the immediate successor of the key.


# Distributed Hash Table
both the number of neighbors per peer as well as the number of messages per query is O(log N), where N is the number of peers.
![](https://lantaoyu.github.io/files/network-figures/finger-table.png)

# Socket
- Socket is locally identified with a port number
- Client needs to know server IP address and socket port number.
- API:
    - BIND: associate a local address (port) with a asocket
    - LISTEN: announce willingness to accept connections
    

# Chapter 3

# TCP and UDP
![](https://lantaoyu.github.io/files/network-figures/tcp-udp.png)
- TCP
    - Flow control matches sender to receiver
    - Congestion control matches sender to network
# Ports
- Servers often bind to “well-known ports”
- FTP (20/21), SMTP (25), POP3 (110), IMAP (143), http (80), https(443).

# Connection-oriented demux: Threaded Web Server
- TCP socket identified by 4-tuple:<br>
(source IP address, source port number, dest IP address, dest port number)

# Connectionless demux
- UDP socket identified by two-tuple:<br>
(dest IP address, dest port number)

# Why UDP?
- no connection establishment (which can add delay)
- no retransmission (which can add delay)
- simple: no connection state at sender, receiver
- small segment header: 8 bytes
- no flow control and congestion control: UDP can blast away as fast as desired
- **Examples**:
    - short message interaction apps: DNS, SNMP, PRC
    - loss tolerant and delay sensitive: ipPhone, SKYPE

# Error detection code (EDC) and retransmission
- Parity checking
    - single bit parity
    - two dimensional bit parity
- Checksum: used in Internet (IP, TCP, UDP), but it is weak
- CRC: cyclic redundancy check
    - Cyclic Redundancy Check used in link layer can detect all burst errors less than r+1 bits
    - Four International Standards Generator Polynomials
    ![](https://lantaoyu.github.io/files/network-figures/crc.png)
    - The power of CRC:
        - all single-bit errors will be detected
        - All two isolated single-bit errors will be detected
        - By making (x + 1) a factor of G(x), all errors consisting of an odd number of inverted bits will be detected
        - all burst errors of length <= r will be detected
    - can be constructed in hardware 
    - CRCs are widely used on links (Ethernet, ADSL, Cable)

# Forwarding Error Correction
- Hamming Code
    - can only correct one bit error
    - used when the error rate is low
- Convolutional codes and LDPC heavily used in wireless data link layer

# Detection vs Correction
- Forward Error Correction:
    - when errors are expected
    - or when no time for transmission
- Error Detection and Retransmission
    - more efficient when errors are not expected
    - burst errors when they do occur

# Reliable Data Transfer
- RDT 1.0:
    - underlying channel perfectly reliable (no error control)
    - receiver has enough buffer and CPU power (no flow control)
- RDT 2.0: channel with errors
    - underlying channel may flip bits in packet (no lost)
    - **checksum** to detect bit errors
    - receiver feedback: control msgs (ACK, NAK)
    - sender retransmits pkt on receipt of NAK
    - **FLAWS**:
        - if ACK/NAK corrupted, sender doesn't know what happened at receiver
        - possible duplicate pkt with retransmission
        - Handling duplicates:
            - sender retransmits current pkt if ACK/NAK garbled
            - sender adds **sequence number** to each pkt
            - receiver discards duplicate pkt
- RDT 2.1： receiver handles garbled ACK/NAKs
- RDT 2.2: a NAK-free protocol
    - instead of NAK, receiver sends ACK for last pkt received OK, receiver must explicitlyinclude seq # of pkt being ACKed
    - duplicate ACK at sender results in same action as NAK: retransmit current pkt

- RDT 3.0: channels with errors and loss
    - sender waits “reasonable” amount of time for ACK
    - requires countdown timer
    - to handle duplicate pkt, receiver must specify seq # of pkt being ACKed
    
# Selective Repeat vs Go-Back-N
- Go-back-N: timer for oldest in-flight pkt
    - cumulative ACK
    - retransmit pkt k and all higher seq# pkts in window when timeout(k)
- Selective Repeat
    - individual ACK
    - sender timer for each unACKed pkt
    - sender only resends pkts for which ACK not received

# Window Overlay Problem
![](https://lantaoyu.github.io/files/network-figures/window-overlay.png)
- To avoid overlapping new receiving window with the original window, the maximum window size should satisfy:<br> 
**sending window + receiving window <= (MAX_SEQ + 1)**

## TCP overview
- end-to-end: no support for multicasting or broadcasting
- reliable byte stream:
    - no “message boundaries”
- hybrid of GBN and SR
    - pipelined segments
    - cumulative and piggyback acks
    - single retransmission timer
    - retransmissions are triggered by
        - timeout events
        - 3 duplicate acks before timer expires: **fast retransmit**
    - only retransmit one segment
- full duplex
- sequence number: byte stream “number” of first byte in segment’s data
- TCP checksum:
    - TCP checksum checks the header, the data, and a pseudo header.
    - The pseudo-header helps detect mis-delivered packets.
    - It also violates the protocol hierarchy since the IP addresses in it belong to the IP layer, not to the TCP layer.

## TCP timer management
- Problem: How do we determine the best timeout value for retransmitting segments in the face of a large standard deviation of round-trip delays?
- Solution: uses **dynamic algorithm** that constantly adjusts the timeout interval, based on continuous measurements of network performance.

## TCP flow control
- announcing window size:the maximum number of bytes that may be sent and received.
- zero window size: sender stop sending. Two exceptions:
    - urgent data
    - 1-byte request for reannounce the window size.

## TCP congestion control
Congestion can be caused by:
- data in burst (app and transport layer)
- lack of capacity/bandwidth (physical layer)
- insufficient memory of routers (network layer)
- slow processors of routers (network layer)

## Congestion Prevention Policies in Open Loop Systems
To achieve congestion control, select appropriate policies at various levels: data link, network, and transport layer.
![](https://lantaoyu.github.io/files/network-figures/congestion-policy.png)
- strategy:
    - predict when congestion is about to happen
    - reduce rate early
- two approaches:
    - host-centric: TCP congestion control
    - Router-centric: warning bit, choke packet, load shedding

## TCP congestion control
- Sender uses **packet loss** as the network congestion signal
    - TCP assume that lost packets are caused by congestion, not by links.
- TCP use a Congestion Window (CongWin)next to the window granted by the receiver. The actual window size is the minimum of the two.
- Algorithm:
    - When CongWin is below Threshold, sender in slow-start phase, window grows exponentially.
    - When CongWin is above Threshold, sender is in congestion-avoidance phase, window grows linearly.
    - When a triple duplicate ACK occurs, Threshold and CongWin set to CongWin/2.
    - When timeout occurs, Threshold set to CongWin/2 and CongWin is set to 1 MSS.
    
## TCP Additive Increase, Multiplicative Decrease (AIMD)
- **additive increase**: increase CongWin by 1 MSS every RTT until loss detected
- **multiplicative decrease**: cut CongWin in half after loss

## When should the slow start (exponential increase) end?
- If there is a loss event:
    - sets the value of congestion window to 1
    - sets the "slow start threshold" to cwnd/2
- when the value of cwnd equals ssthresh, slow start ends and TCP transitions into congestion avoidance mode.

## when should congestion avoidance’s linear increase (of 1 MSS per RTT) end?
- a timeout occurs
    - The value of cwnd is set to 1 MSS, and the value of ssthresh is updated to half the value of cwnd
- a triple duplicate ACK event
    - TCP halves the value of cwnd
    - the value of ssthresh to be half the value of cwnd

## TCP throughput
- Under assumptions, Because TCP’s throughput (that is, rate) increases linearly between the two extreme values, we have:<br>
average throughput = 0.75 * W / RTT
- the throughput of a TCP connection as a function of the loss rate (L), the round-trip time (RTT), and the maximum segment size (MSS):<br>
![](https://lantaoyu.github.io/files/network-figures/tcp-throughput.png)

## TCP fairness
- A congestion-control mechanism is said to be fair if the average transmission rate of each connection is approximately R/K; that is, each connection gets an equal share of the link bandwidth.

# Chapter 4
## Network Layer Function:
- **glue/interconnect** lower-level networks together: allow packets to be sent between any pair of hosts
- network layer provides either host-to-host connectionless service or host-to-host connection service, **but not both.**
- connection service => virtual circuit (VC) networks
- connectionless service => datagram networks
- network-layer connection service is **implemented in the routers in the network core as well as in the end systems**
- Internet is a datagram network.

## Router Functions:
- routing
- forwarding/switching
- congestion control: drop packets, update routing table

## Implementation
- Router Forwarding Plane are typically implemented in **hardware**.
- ROuter Control Plane are typically implemented in **software**.

## Virtual Circuit
- VC consists of:
    - path from source to destination
    - VC numbers, one number for each link along the path
    - entries in routers along path
- Packet carries VC number rather than destination address as the index of forwarding
- VC number can be changed on each link
- Routers maintain connection state information

## Why not keep the same VC number?
- replacing the number from link to link reduces the length of the VC field in the packet header.
- **VC setup is considerably simplified** by permitting a different VC number at each link along the path of the VC

## Router (four parts)
- input port
- output port
- routing processor
- switching fabric

## Input port function
- physical layer
    - bit-level reception
- data link layer
    - processing (protocol, decapsulation)
- network layer
    - lookup, forwarding, queuing

## Three types of switching
- memory: The simplest, earliest routers were traditional computers,
with switching between input and output ports being done under direct control of the CPU (routing processor). An input port with an arriving packet first signaled the routing processor via an interrupt. The packet was then copied from the input port into processor memory. The routing processor then extracted the destination address from the header, looked up the appropriate output port in the forwarding table, and copied the packet to the output port’s buffers.
- bus: If multiple packets arrive to the router at the same time, each at a different input port, all but one must wait since only one packet can cross the bus at a time.
- interconnection network: A crossbar switch is an interconnection network consisting of 2N buses that connect N input ports to N output ports. If two packets from two different input ports are destined to the same output port, then one will have to wait at the input, since only one packet can be sent over any given bus at a time.

## Output ports
- switch fabric -> queuing (buffer management) -> data link processing (protocol, decapsulation) ->line termination

## Input port queuing
- fabric slower than input ports combined -> queuing may occur at input queues
- **head-of-the-Line (HOL) blocking**: queued datagram at front of queue prevents others in queue from moving forward

## Output Port Queuing
- buffering when arrival rate via switch exceeds output line speed

## Buffer design
- how much buffer? rule of thumb
    - RTT; round-trip time; C: link capacity; N: number of TCP flows
    - average buffer = RTT * C
    - recent recommendation: with N flows, buffer equal to $RTT * C / \sqrt{N}$

## Internet's network layer
- IP protocol
- routing component: routing protocols compute the forwarding tables that are used to forward packets through the network
- a facility to report errors in datagrams and respond to requests for certain network-layer information: Internet Control Message Protocol (ICMP)

## Datagram format
![](https://lantaoyu.github.io/files/network-figures/ipv4.png)
- protocol: This field is used only when an IP datagram reaches its final destination. The value of this field indicates the specific transport-layer protocol to which the data portion of this IP datagram should be passed. A value of 6 indicates that the data portion is passed to TCP, while a value of 17 indicates that the data is passed to UDP.

## Header length
- IP header: 20 bytes
- TCP header: 20 bytes

## MTU
The maximum amount of data that a link-layer frame can carry is called the maximum transmission unit (MTU).


## IP fragmentation and reassembly
- Reassembling is done in end systems rather than routers.
- maximum transmission unit (MTU) of link layer puts a hard limit to the size of IP datagram
- the designers of IPv4 decided to put the job of datagram reassembly in the end systems rather than in network routers
- _identification, flag, fragmentation_ field in the header
- in order for the destination host to be absolutely sure it has received
the last fragment of the original datagram, the last fragment has a flag bit set to 0,
whereas all the other fragments have this flag bit set to 1.
- At the destination, the payload of the datagram is passed to the transport layer
only after the IP layer has fully reconstructed the original IP datagram. If one or
more of the fragments does not arrive at the destination, the incomplete datagram is
discarded and not passed to the transport layer
- Example:<br>
A datagram of 4,000 bytes (20 bytes of IP header plus 3,980 bytes of IP payload) arrives at a router and must be forwarded to a link with an MTU of 1,500 bytes.
![](https://lantaoyu.github.io/files/network-figures/ip-fragments.png)


## IP header options
- security: specifies how secret the datagram is.
- strict source routing: gives the complete path to be followed
- loose source route: gives a list of routers not to be missed
- record route: makes each router append its IP address
- Timestamp: makes each router append its timestamp and address

## IP address
- 32 bit identifier for interface of routers and hosts
- written in dotted decimal
- must be globally unique for globally access
- IP requires each host and router interface to have its own IP address. Thus, an IP address is technically associated with an interface, rather than with the host or router containing that interface.

## Subneting
- IP network: all computers addressed with a common identical network id
    - an IP network is a broadcasting network
    - multiple IP networks are interconnected by routers or 3-layer  switch (VLAN)

- Problem with large IP networks:
    - different computers are administratively controlled by different entities
    - broadcasting storm

- solution: dividing an IP network into two or more networks is called subnetting

- What's a subnet?
    - device interfaces with same subnet part of IP address
    - can physically reach each other without intervening routers

- **subnet mask**: 223.1.1.0/24, indicates that the leftmost 24 bits of the 32-bit quantity define the subnet address.


## Classless IP Addressing
- VLSM: variable length subnet mask
- IP address = subnet id + host id
- subnet mask: to indicate the subnet portion which is variable length
    - a.b.c.d/x, where x is # bits in subnet portion of address
    - 1 for subnet id bits, 0 for host id bits (e.g. 255.255.255.0)

## The Internet’s address assignment strategy: CIDR (Classless InterDomain Routing)
- problem: routing table explosion
- assign class C addresses in **contiguous blocks** of 256 addresses so that multiple entries in routing table can be aggregated into one (reduced)
- Contiguous blocks of IP addresses with **common prefix** and **the whole range** of that prefix could be aggregated into one route entry.
- Even if there is **a hole** in the blocks of IP addresses the common prefix could still be aggregated with another **longer prefix for the hole**.

## IP broadcast address
When a host sends a datagram with destination address 255.255.255.255, the message is delivered to all hosts on the same subnet. Routers optionally forward the message into neighboring subnets as well

## DHCP: Dynamic Host Configuration Protocol
- For obtaining a host address
- Four steps:
    - **DHCP server discovery**: the DHCP client
creates an IP datagram containing its DHCP discover message along with the
broadcast destination IP address of 255.255.255.255 and a “this host” source IP
address of 0.0.0.0.
    - **DHCP server offer(s)**: A DHCP server receiving a DHCP discover message
responds to the client with a DHCP offer message that is broadcast to all nodes
on the subnet, again using the IP broadcast address of 255.255.255.255
    - **DHCP request**: The newly arriving client will choose from among one or more
server offers and respond to its selected offer with a DHCP request message,
    - **DHCP ACK**: The server responds to the DHCP request message with a DHCP ACK message, confirming the requested parameters.

## NAT: Network Address Translation
- Motivation: hosts in LANs use private IP address and share one public IP address for internet access
    - handle public IP address shortage
    - can change address of devices in LAN without notifying outside world
    - can change ISPs without changing addresses of devices in LANs
    - devices inside not explicitly addressable, visible by outside world (a security plus)
- uses 16 bit port field
- The NAT-enabled router does not look like a router to the outside world. Instead
the NAT router behaves to the outside world as a single device with a single IP
address.
- NAT is controversial:
    - violates independence layering principles
    - violates end-to-end argument
        - NAT traversals must be taken into account by app designers
    - address shortage should instead be addressed by IPv6

## NAT Traversal Problem
- Solution 1: **statically configure NAT** to forward incoming connection requests at given port to server
- Solution 2: Universal Plug and Play:
With UPnP, an application running in a host can request a NAT mapping between its (private IP address, private port number) and the (public IP address, public port number) for some requested public port number.
In summary, UPnP allows external hosts to initiate communication sessions to NATed hosts, using either TCP or UDP.
- Solution 3: relaying (used in Skype)
    - NATed client establishes connection to relay
    - External client connects to relay
    - relay bridges packets between to connections

## ICMP
- Internet Control Message Protocol
- ICMP is often considered part of IP but architecturally it lies just above IP, as ICMP messages are carried inside IP datagrams. That is, ICMP messages are carried as IP payload
- Note that ICMP messages are used not only for signaling error conditions.

## IPv6
- initial motivation: 32 bit address space soon to be completely allocated
- additional motivation: 
    - header format helps speed processing/forwarding
    - header changes to facilitate QoS
- IPv6 datagram format:
    ![](https://lantaoyu.github.io/files/network-figures/ipv6.png)
    - fixed length 40 byte header
    - extension header allowed
- IPv6 increases the size of the IP address from 32 to 128 bits
- The resulting 40-byte fixed-length header allows faster processing of the IP datagram

## Comparison of IPv4 and IPv6
- IPv4: 20+ byte headers, 12 + 1 fields
- IPv6: 40 byte headers, 8 fields


## Routing Algorithm classification
- global: 
    - all routers have complete topology and link cost information
    - **link state algorithm**
- local:
    - routers knows link costs to neighbours, exchange of info with neighbors
    - **distance vector algorithm**
- static:
    - routers change slowly over time
- dynamic:
    - routers change more quickly
    - periodic update
    - in response to network topology and link costs changes
- Internet routing algorithms (such as RIP, OSPF, and
BGP) are load-insensitive, as a link’s cost does not explicitly reflect its current (or
recent past) level of congestion.

## Routing algorithms
## Link state routing (LSR): 
- Each router learns the entire network topology through exchanging information with all other routers, and then calculate least cost path to the other routers.
- Dijkstra’s algorithm to build the sink tree
    - The number of times the loop is executed is equal to the number of nodes in the network.
    ![](https://lantaoyu.github.io/files/network-figures/LS.png)

## Distance Vector Routing / Bellman-Ford
- Each router maintains a table (i.e Distance Vector) with least cost/distance to every other routers.

## Comparison between LSR and DVR
- message complexity:
    - LSR: with n nodes, E links, O(nE) messages sent totally, O(n^2) complexity
    - DVR: exchange between neighbors only, O(n) totally

- computation complexity:
    - LSR: O(n^2) each node
    - DVR: O(n) each node

- speed of convergence:
    - LSR: 1 iteration, may have oscilliations
    - DVR: n iterations
        - good news travel fast
        - count-to-infinity problem
- updating when:
    - local link cost change
    - LS/DV update message from others/neighbors
    - periodically
- Neither algorithm is an obvious winner over the other; indeed, both algorithms are used in the Internet.

## Hierarchical Routing
- **Autonomous System (AS)**: aggregate routers into regions, correspond to an administrative domain. Assigned an unique 16/32 bit number
- **intra-AS/interior gateway routing** should find the least cost path as best as possible
    - routers in same AS run same routing protocol
    - routers in different AS can run different intra-AS routing protocol
- **inter-AS/exterior gateway routing** has to deal with a lot of politics. Routers do not automatically use the routes they find, but have to check manually whether it is allowed.
- Why different intra-AS, inter-AS routing?
    - policy: 
        - inter-AS: admins want to have control over how its traffic routed, and who routes through its net. (untrusted)
        - intra-AS: single admin, so no policy decisions needed (trusted)
    - scale: hierarchical routing saves table size, reduced update traffic
    - performance:
        - intra-AS: can focus on performance
        - inter-AS: policy may dominate performance

## Routing in the internet - Hierarchical
- most common intra-AS routing protocols
    - RIP: Routing Information Protocol
    - OSPF: Open Shortest Path First
    - IGRP: Interior Gateway Routining Protocol
- most common inter-AS routing protocols
    - BGP: Border Gateway Protocol

## RIP (Routing Information Protocol)
- Distance Vector Algorithm
- DV advertisement exchanged among neighbors every 30 sec in UDP packets
- In RIP (and also in OSPF), costs are actually from source router to a **destination
subnet**. RIP uses the term hop, which is **the number of subnets** traversed
along the shortest path from source router to destination subnet, including the destination
subnet.
- distance metric: # of hops, Limits networks to 15 hops (16 = inf to avoid count-to-infinity)

## OSPF (Open Shortest Path Protocol)
- "open": the routing protocol specification is publicly available
- OSPF is a link-state protocol that uses flooding of link-state information and a Dijkstra least-cost path algorithm
- OSPF advertisements disseminated to entireAS
- **hierarchical OSPF** in large domains

## RIP and OSPF
- OSPF and its closely related cousin, IS-IS, are typically deployed in upper-tier ISPs
- RIP is deployed in lower-tier ISPs and enterprise networks


## Hierarchical OSPF
- An OSPF autonomous system can be configured hierarchically into areas. Each
area runs its own OSPF link-state routing algorithm, with each router in an area
broadcasting its link state to all other routers in that area.
- two level hierarchy:
    - local area: run OSPF
    - backbone: area 0
- four kinds routers
    - internal routers (IR)
    - area border routers (ABR): Within each area, one or more area border routers are responsible for routing packets outside the area
    - backbone routers (BaR): exactly one OSPF area in the AS is configured to be the backbone area. The primary role of the backbone area is to route traffic between the other areas in the AS
    - boundary routers (BoR)

## Border Gateway Protocol
- advertised prefix includes BGP attributes
- route = prefix + AS-path + Next-hop
- router may learn about multiple routes to some prefix. Router must select one from the routes.
- ordered selection rules (for good instead of best route):<br>
1. Local preferences (policy)
2. Shortest AS-path
3. Closet next hop router
4. Additional criteria


## Broadcast and multicast routing
## broadcast routing:
- deliver packets from source to all other routers
- source duplication is inefficient
- in-network duplication can be more efficient with controlled duplicate transmission
- **flooding**: when node receives brdcst pckt, sends copies to all neighbors
- **controlled flooding**: node only brdcsts pkt if it hasn’t brdcst same packet before
    - node keeps track of pckt IDs already brdcsted
    - **reverse path forwarding (RPF)**: only forward pckt if it arrived on shortest path between node and source
- spanning tree: no redundant packets received by any nodes
    - nodes forward copies only along spanning tree
    - Pro: makes excellent use of bandwidth
    - Con: each router must have knowledge of some spanning tree

## Multicast Routing
- goal: find a tree (or trees) connecting routers having local mcast group members
    - **source-based**: different tree from each sender to rcvrs
    - **shared-tree**: same tree used by all group members
- IP multicasting uses **class D** addresses
- Each class D address identifies a group of hosts.
- Groups are managed using **IGMP (Internet Group Management Protocol)**
    - operates between a host and its directly attached router
- Network-layer multicast in the Internet consists of two complementary components: IGMP and multicast routing protocols.
- Intra-AS Multi-cast Routing Protocols
    - Distance-Vector Multicast Routing Protocol (DVMRP) uses an RPF algorithm with pruning
    - Protocol-Independent Multicast (PIM) routing protocol
        - **dense mode** based on pruned RPF
        - **Sparse mode** based on pruned spanning tree
- Inter-AS Multi-cast Routing Protocols
    - extensions to BGP to allow it to carry routing information for other protocols, including multicast information
    - MSDP(Multicast Source Discovery Protocol) to connect centers in PIM sparse mode


# Chapter 5 The Data Link Layer

## Checksum
- In the TCP and UDP protocols, the Internet checksum is computed over all fields (header and data fields included). 
- In IP the checksum is computed over the IP header (since the UDP or TCP segment has its own checksum).

## Data link layer
- Data link layer is the place in the protocol stack where software meets hardware (firmware)
- implemented in adapter (network interface card NID) in each host and routers
- Data-link layer has responsibility of transferring datagram from one node to **physically adjacent** node over a link (node-to-node job)
- Datagram transferred by **different link protocols** over multiple links from source to destination.
- point-to-point link protocols
    - PPP
    - HDLC
- broadcast link protocols
    - Ethernet
    - IEEE802.3

## Data Link Layer Services
- framing: encapsulate datagram into frame, adding **header, trailer**
- reliable date transfer between adjacent nodes
- link access for shared medium
    - Medium/Multiple Access Control (MAC)
    - "MAC" addresses: used in frame headers to identify source, destination
    
## Two point-to-point Data Link Protocols
- HDLC (High-Level Data Link Control): 
    - **bit-oriented**
    - **supports flow control and error control**
- PPP (The Point-to-Point Protocol):
    - Internet standard (RFC1661 1662 1663), is used in the Internet for a variety of purposes, including router-to-router traffic and home user-to-ISP traffic. 
    - **byte-oriented**
    - PPP is a variant of HDLC **without flow/error control**, supporting multiple upper layer protocols
    - PPP uses **LCP** to manage links and uses **NCP** to negotiate network-layer options

## Ideal MAC Protocol
- for broadcast channel of rate R bps:
    - efficient: when one node wants to transmit, it can send at rate R.
    - fair: when M nodes want to transmit, each can send at average rate R/M
    - fully decentralized:
        - no special node to coordinate transmissions
        - no synchronization of clocks, slots
    - simple

## Three broad classes of MAC protocols
- Channel Partitioning (static)
    - divide channel into smaller “pieces” (TDM, FDM, CDM)
    - allocate piece to node for **exclusive use**
- Random Access (dynamic)
    - channel not divided, allow collisions
    - "recover" from collisions
- Taking turns (dynamic)
    - nodes take turns
    - nodes with more to send can take longer turns
    
## Random Access MAC Protocol
- random access:
    - transmit at full channel data rate R When node has packet to send
    - no priori coordination among nodes, possible collision
-  random access MAC protocol specifies:
    - how to detect collisions
    - how to recover from collisions (e.g., via delayed retransmissions)
- Examples :
    - ALOHA, slotted ALOHA
    - CSMA, CSMA/CD, CSMA/CA

## ALOHA
- Nodes transmit immediately whenever data is ready in **pure ALOHA**
    - collision possible, retry after a random amount of time.
    - frame sent at t0 collides with other frames sent in [t0-1,t0+1]
    - Maximum efficiency of Pure ALOHA is 0.18
- Nodes transmit at the beginning of next slot whenever data is ready in **slotted ALOHA**
    - Maximum efficiency of slottedALOHA is 0.36
- Problem: a node’s transmission decision is **independent of** other nodes’ activities

## CSMA (Carrier Sense Multiple Access)
listen before transmit:
- If channel sensed idle: transmit entire frame
    - p-persistent: transmit with probability p, and defer until next slot with probability 1-p.
- If channel sensed busy, defer transmission
    - 1-persistent: keeping sensing and immediately start transmission when idle
    - nonpersistent: wait a random period of time before trying again

## Link-Layer Addressing
- Each adapter in LAN has 48 bit, permanent, globally unique MAC address
- MAC addresses are burned in NIC ROM
- **ARP (Address Resolution Protocol)** is used to translate IP address into MAC address

## Ethernet efficiency
- Ethernet (bus) efficiency is better than ALOHA, but deteriorates as bit-rate and distance raise
![](https://lantaoyu.github.io/files/network-figures/ethernet.png)
- Ethernet or CSMA/CD is unsuitable for high speed and long distance networks.

## Collision Region (CR) and Broadcast Region (BR)
- Use switch to reduce the collision region
- Use router to reduce the broadcasting region and connect with Internet.

## Virtual LAN
- Use switch to reduce the broadcasting region with less overhead and more flexibility
- Multiple VLANs over single switch are different broadcast domains
- VLAN can span multiple switches from different physical location
- VLANs isolate broadcast domains, could only connected by routing

# Chapter 6 Wireless and Mobile Networks
- The 802.11(**WiFi**) is the wireless version of 802.3 (Ethernet) , but **much different in physical and data link layer**.
    - all use CSMA/CA for multiple access
    - all have base-station and ad-hoc network versions

- 802.15: Bluetooth Architecture
    - TDD(Time Division Duplexing) : The master in each piconet defines a series of 625 μsec time slots, with the master getting half the slots and the slaves sharing the other half.
