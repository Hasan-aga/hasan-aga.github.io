---
title: 'NS3: the second step forward'
description: Using Ping with a P2P network.
date: '2020-07-13T16:09:53.135Z'
categories: []
keywords: []
slug: /@hasan-alsulaiman/ns3-the-second-step-forward-9ca17333b33
---

In the last example we created a simple LAN network, now we will create something a little more convoluted.

![](/assets/0__D__PfuFUf6tfYB____w.jpg)
)
### The Topology:

I will build my application on NS3 tutorial number [three](https://www.nsnam.org/docs/tutorial/html/building-topologies.html#building-a-wireless-network-topology), but instead of using Echo I will use Ping,

We will make two networks and connect them together using a P2P connection, one of them is a wireless network, the other is LAN

Then, to simulate our design, we will have one wireless device _ping_ a LAN device

  _Wifi 10.1.3.0_

                _AP_

 _\*    \*    \*    \*_

 _|    |    |    |    10.1.1.0_

 _n5   n6   n7   n0-----------------n1   n2   n3   n4_

                   _point-to-point  |    |    |    |_

                                   _================_

                                     _LAN 10.1.2.0_

Basically we go through the same procedure described in the [last example](https://medium.com/@hasanali_80640/simple-ns3-example-one-lan-6ce8ef2ff024) the difference this time is:  
1\. using WiFi   
2\. using Mobility to simulate moving WiFi users  
3\. using Ping instead of Echo

first let’s look at the whole program and then we will go through it explaining each major step:

We started by importing the necessary modules as we always do, we then made a function called “PingRtt” that we will later use to log the Ping results of our simulation, I don’t quite understand how we retrieved the rtt value though,

PingRtt (std::string context, Time rtt){                         std::cout << context << " " << rtt << std::endl;                       }

We then move to the main function, here we create two P2P nodes, configure the P2P channel and add nodes to the channel after installing them as devices

#### Point-to-point (P2P):

// create the p2p nodes                          
 NodeContainer p2pNodes;                          
 p2pNodes.Create (2);                           
// setup p2p channel                           
PointToPointHelper pointToPoint;                         pointToPoint.SetDeviceAttribute ("DataRate", StringValue ("5Mbps"));                         pointToPoint.SetChannelAttribute ("Delay", StringValue ("2ms"));                         // install p2p device on the p2p nodes                         NetDeviceContainer p2pDevices;                          
 p2pDevices = pointToPoint.Install (p2pNodes);                         

#### Local Area Network (LAN):

We move on to create the csma (LAN) network, here we grab one of the rightmost P2P node (n1) and add to the list of csma nodes that we will create, the number of nodes here is set by the _nCsma_ variable, then we continue by configuring the csma channel and installing the nodes on it as devices,

// create LAN nodes by adding one of the p2p nodes to a group of new nodes                          
NodeContainer csmaNodes;                           
csmaNodes.Add (p2pNodes.Get (1));                         csmaNodes.Create (nCsma);                           
// setup LAN channel                           
CsmaHelper csma;                           
csma.SetChannelAttribute ("DataRate", StringValue ("100Mbps"));                         csma.SetChannelAttribute ("Delay", TimeValue (NanoSeconds (6560)));                         // install LAN devices on LAN nodes                         NetDeviceContainer csmaDevices;                           
csmaDevices = csma.Install (csmaNodes);

#### WiFi:

The WiFi network is made up of two types of WiFi devices: Access point and Station, so we have to create two groups of nodes, one group that will become stations, and one node that will be the access point, we are going to use the leftmost P2P node (n0) as our access point

NodeContainer wifiStaNodes;                         wifiStaNodes.Create (nWifi);                           
NodeContainer wifiApNode = p2pNodes.Get (0);

Next we configure the WiFi channel and physical layer settings, for simplicity we are using default settings.

YansWifiChannelHelper channel = YansWifiChannelHelper::Default ();                         YansWifiPhyHelper phy = YansWifiPhyHelper::Default ();                         phy.SetChannel (channel.Create ());

We move on to the MAC layer, here we tell the _WiFiHelper_ that we will use _AARF_ rate control algorithm,

WifiHelper wifi;                         wifi.SetRemoteStationManager ("ns3::AarfWifiManager");

Next, we set the SSID and some other MAC settings, notice that we are dealing with the _Station_ settings, hence the “sta” in _StaWifiMac_

WifiMacHelper mac;                           
Ssid ssid = Ssid ("ns-3-ssid");                           
mac.SetType ("ns3::StaWifiMac", "Ssid", SsidValue (ssid), "ActiveProbing", BooleanValue (false));                           
  

Next, we create station devices using the settings we made (phy, mac) and the station nodes (wifiStaNodes)

NetDeviceContainer staDevices;                           
staDevices = wifi.Install (phy, mac, wifiStaNodes);

We move to set the _Access-point settings,_

mac.SetType ("ns3::ApWifiMac", "Ssid", SsidValue (ssid));

Then we create access-point device using which has the same Physical-layer and channel attributes as the stations,

NetDeviceContainer apDevices;                           
apDevices = wifi.Install (phy, mac, wifiApNode);

#### Mobility:

We can make our station devices move around to simulate actual WiFi station device behavior, we do that with the mobility helper, notice that the AP device remains stationary,  
the `_SetPositionAllocator_` class places the nodes on an initial grid,

MobilityHelper mobility;                                                 mobility.SetPositionAllocator ("ns3::GridPositionAllocator", "MinX",          DoubleValue (0.0), "MinY",                                                 DoubleValue (0.0), "DeltaX", DoubleValue (5.0), "DeltaY",                                                        DoubleValue (10.0), "GridWidth", UintegerValue (3), "LayoutType",                                                     StringValue ("RowFirst"));

After placing the nodes on an initial grid we need to tell them how to move, this is what `_RandomWalk2dMobilityModel_` which makes our nodes move inside a box at a random speed

mobility.SetMobilityModel ("ns3::RandomWalk2dMobilityModel", "Bounds",                                                    RectangleValue (Rectangle (-50, 50, -50, 50)));

Next, we install the mobility models on the Station nodes

mobility.Install (wifiStaNodes);

But we need the AP to remain in a fixed position, so we use:

mobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");                         mobility.Install (wifiApNode);

#### Internet Stack

Next we install internet stack on all devices:

InternetStackHelper stack;    
stack.Install (csmaNodes);    
stack.Install (wifiApNode);    
stack.Install (wifiStaNodes);

#### IP Addresses

Ping uses IP addresses so before installing a Ping Program we first need to config IP addresses for our devices:

Ipv4AddressHelper address;     
address.SetBase ("10.1.1.0", "255.255.255.0");  Ipv4InterfaceContainer p2pInterfaces;    
p2pInterfaces = address.Assign (p2pDevices);     
address.SetBase ("10.1.2.0", "255.255.255.0");  Ipv4InterfaceContainer csmaInterfaces;    
csmaInterfaces = address.Assign (csmaDevices);     
address.SetBase ("10.1.3.0", "255.255.255.0");    
address.Assign (staDevices);    
address.Assign (apDevices);

#### Ping

Using [this](https://www.nsnam.org/doxygen/csma-ping_8cc_source.html) example as a guide I managed to install and use Ping on my topology.

We now install the Ping program on one of our devices and have it ping a device on the other network, the process of configuring the ping helper function involves passing the IP address of the destination device as follows:

V4PingHelper ping = V4PingHelper (csmaInterfaces.GetAddress (nCsma));

the line `_csmaInterfaces.GetAddress(nCsma)_` simply tells the function to look inside the _csmaInterfaces_ variable (which we created in the IP configuring process above) and get the IP address of interface whose number corresponds to whatever value inside the variable _nCsma,_

We now create new nodes, these can be used to specify the list of devices on which we want to install the Ping application, for now we only choose one device

NodeContainer pingers;  
pingers.Add (wifiStaNodes.Get (0));

_wifiStaNodes.Get (0)_ will select n0 from the list of WiFi nodes and add it to the list named _pingers,_

Next we simply install the ping program on the devices whatever devices we kept in the variable _pingers,_ then we start the ping app and stop it at specific simulation times,

ApplicationContainer apps = ping.Install (pingers);    
apps.Start (Seconds (2.0));    
apps.Stop (Seconds (9.0));

#### The End Is Near! 💩

Whats left of our code is a command used to fill the routing tables automatically (this is faster than actually adding a router and configuring it)

Ipv4GlobalRoutingHelper::PopulateRoutingTables ();

Then we have an if-statement which when _True_ would enable tracing, what is tracing?   
it is generating network data from our devices that we can examine in a program such as WireShark.

The final step is to print the output of the ping we made on the terminal, for that we use the _PingRtt_ function we created which in turn uses _cout_ to log the results to the terminal,

Config::Connect ("/NodeList/\*/ApplicationList/\*/$ns3::V4Ping/Rtt", MakeCallback (&PingRtt));

To be honest I dont fully understand how the function retrieved the Rtt 🤷‍

Anyway, we just spent five hours to create something that would’ve took us 5 minutes with any other simulator 😒  
the advantage is that everything here is written in C++ and we have direct access to it, so we have a lot of room to test things, for example, you can write your own ping program! idk why you would want to do that, but if you did, you could 😎