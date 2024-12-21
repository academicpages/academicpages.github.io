---
title: "kmdfHelloWorldDriver"
excerpt: "This project involved creating a Universal Windows driver using the Kernel-Mode Driver Framework (KMDF), deploying it to a Hyper-V virtual machine, and debugging it with WinDbg. I gained hands-on experience with driver deployment, kernel debugging, and system-level interactions.<br/><img src='/images/exampleDriverCode.png'>"
collection: portfolio
---

04 April 2024
# Creating The Driver

For this project I prepare a small Universal Windows driver using the Kernel-Mode Driver Framework (KMDF) and then I deploy it and install it on a virtual machine inside of Window’s HyperV component.

To begin the drivers code it is important to include necessary headers/ includes.

In this case:

    #include <ntddk.h> // “Contains core Windows kernel definitions for all drivers”
  	#include <wdf.h> // “Contains definitions for drivers based on the Windows Driver Framework (WDF)

Then I plan to use two methods, so I declare two prototypes for them before the entrypoint:

```c
//declarations for the callbacks we'll use
  DRIVER_INITIALIZE DriverEntry;
  EVT_WDF_DRIVER_DEVICE_ADD KmdfHelloWorldEvtDeviceAdd;
```

Following these, it’s time to declare the entrypoint for our driver, which we’ll call “DriverEntry”.

```c
NTSTATUS DriverEntry(
	_In_ PDRIVER_OBJECT DriverObject,
	_In_ PUNICODE_STRING RegistryPath
)
```

**NTSTATUS** as a return type is crucial because it indicates success or failure, & usually useful debugging information such as diagnostic codes.

>Both **DriverObject** and **RegistryPath** are needed parameters for the DriverEntry entrypoint function as seen on Microsoft’s official documentation.

>>**DriverObject** is a ptr to a structure that represents the Windows Driver Model driver object.

>>**RegistryPath** here is a ptr to a structure that specifies the path to the driver’s parameters in the registry.

Furthermore - as I defined this method I tried to comment as best as I could to explain what is happening.

![DriverEntry](https://i.imgur.com/DBIQL4R.png)

As seen in the WDF_DRIVER_CONFIG_INIT function I pass a ptr to the drivers EntDriverDeviceAdd method which is defined below.

![KmdfHelloWorldEvtDeviceAdd](https://i.imgur.com/nbcfAKP.png)

I show you all of this to to prove the primary content of a kernel level driver is usually just a grouping of functions, that just sit there and wait for an event or the system to call them to perform some action.

### Examples:
+ New Device Arrival Event
+ Input/ Output Request from a usermode application
+ A system event (such as a poweroff)
+ A request from another driver/ syscall

# Debugging Drivers On Seperate Computers

+ Introduction
  + Debugging drivers often involves using separate computers: a host and a target.
  + The host computer debugs the target, which is crucial because driver debugging deals with entire machine operations, not just single applications.

+ Host Computer
  + The host computer is where debugging tools are run.
  + Debugging on the host isolates the target, reducing risks and maintaining stability.
  + It enables real-world testing by simulating driver behavior in its intended environment.
  + Access to hardware resources is facilitated for thorough debugging.
  + Kernel debugging capabilities are provided, granting special execution privileges for in-depth analysis.

+ Target Computer
  + The target computer runs the operating system and the driver being debugged.
  + It represents the real-world environment for observing driver interactions.
  + Debugging on the target ensures isolation from the host, preventing destabilization.
  + It allows direct access to hardware resources required for debugging tasks.
  + Kernel debugging functionalities are utilized for troubleshooting kernel-mode components.

# Driver Deployment (to target machine)

Now we set up the deployment aspect of this driver. In visual studio, we have an option to deploy a driver using the network. Which is what I used in this project. To get the driver to my target machine.

![DeploymentSettingsInVisualStudio](https://i.imgur.com/bWOEJwk.png)

As you can see I am using the network to deploy my driver in the network, I am providing the PC name as the network host and communicating over port 52390.

**Below I am pinging the target machine to ensure communication.**

![PingingEnsuringCommunication](https://i.imgur.com/TdDkjRS.png)

However this communication over the network wasn’t working at first, so I had to go into the firewall settings. As shown below - and for all **Inbound Rules** with a **Profile** of **“Private”**, I had to change a setting in order to fulfill communication between my two devices.

![FirewallInboundRules](https://i.imgur.com/4KcOzLx.png)

Inside of these base profiles of private, all I had to do was make sure that under Scope > Remote IP Address it was set to Any IP address. In contrast to the option below.

![RemoteIpAddressFirewallSettings](https://i.imgur.com/2UQmoAq.png)

After manipulating these settings, I finally got the driver to deploy on my target VM as shown here.

![DriverOnTargetMachineProof](https://i.imgur.com/Fm8HZ4y.png)

The KmdfHelloWorld.sys is the actual driver here.

# Installing The Driver - After Deployment

## Service Creation Method

At first I tried to install this driver by creating a service of type kernel and running the service.

![ServiceCreationMethod](https://i.imgur.com/l9w2Eu3.png)

However, the guide which I followed to create the driver does it a different way than the book I am reading, so I wanted to do it both ways. I prefer this way though.

The guide uses a tool called *DevCon* utility located inside the Windows Development Kit installation path to install this driver.

## Devcon Utility Method

![DevconUtilityMethod](https://i.imgur.com/LsAmZ17.png)

As you can see it created a device node, and prompted me if I wanted to install this driver. Which I did. :D

![Success](https://i.imgur.com/DVKOMd6.png)

Success! Now in order to 100% guarantee that the driver is installed I wanted to see it whilst debugging.

# Debugging The Driver

To debug a driver, you can either use WinDbg, or WinDbg preview which is just a newer release (has a much better user interface).

The first task though to be able to debug is to enable debugging in the command prompt via the command: **bcdedit /debug on**, or else a connection will not establish.

Then I needed to set adjust some basic settings, in both the command prompt on the target machine and in WinDbg on the host machine.

#### Target Machine:

![TargetMachine](https://i.imgur.com/RwaZIE9.png)

#### Host Machine:

![HostMachine](https://i.imgur.com/6rgL1lL.png)

Which then allowed me to attach to the target machines kernel and set a breakpoint on the entire machine.

![WinDbgConnection](https://i.imgur.com/vuguGhw.png)

Now that I’ve got a connection to the kernel I can load the modules and see that I’ve successfully installed and got the kmdfHelloWorldDriver loaded and working.

![LoadedModules](https://i.imgur.com/U3fcGcR.png)

Finally to finish it all off I just wanted to confirm my output via kdPrint was working, and here is a picture of that through DbgView.

![TheEnd](https://i.imgur.com/FipAh8Y.png)

# The End!
