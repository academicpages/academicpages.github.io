---
title: 'Arch Notes - First Linux Experience'
date: 2023-12-23
permalink: /posts/2023/12/arch-notes-1/
tags:
  - linux
  - arch
  - operating systems
  - tutorial
  - linux-beginner
---
These are my notes on [Arch](https://archlinux.org/) from when I first installed it. I've never used Linux before this.

# Preface
I entered a Linux 'rabbithole' during college winter break and decided to start transitioning to a Linux based operating system (OS) from the Windows OS that I use now. Arch seemed to be the best fit for me and I decided to make a virtual machine (VM) and install it (without `archinstall`).

I have experience with concepts that help me understand how an OS works from some computer science courses, so it's probably easier for me to conceptualize exactly what I'm doing and how the OS works than most others without that type of experience. However, I think there is enough content (or close to) to take anyone from knowing almost nothing about details like schedulers, file systems, partitions, swapping, etc. to having a solid conceptual grasp as to what makes up an OS.

## P.1 - Notes
These notes are primarily taken from the [Arch Wiki](https://wiki.archlinux.org/). Various external resources are scattered throughout from my time undergoing the installation process. In these notes I include excerpts, paraphrases, expansions, or explanations in my own words which I hope makes this process productive and effective. I _highly_ recommend reading the Wiki thoroughly if you have questions. I know, everyone says "It's in the Wiki", but odds are it really is. The installation wiki can seem vague and opaque, but it isn't if you understand everything it is _saying_. Hence, understanding the *commands* and *terminology* is super important. The Wiki docs on the commands was much more helpful that I expected. Read the Wiki pages on each command if you don't know exactly what it is doing. Click on the links it provides and don't shy away from spending time reading on them. My notes provide lots of additional resources that maybe aren't necessary, but are more accessible to someone who might have a bit of trouble peeling through fine text word by word.

Another huge resource for these notes is the [Arch Linux Installation Guide (Best on Youtube)](https://www.youtube.com/watch?v=rUEnS1zj1DM) by Mental Outlaw. The information provided in this video is a bit dated but is a great resource as long as you check with the Arch Wiki and also read some of the top comments.

If you plan on watching a video tutorial like I did in addition to using the Arch Wiki, just be wary that some things might be outdated or wrong. When in doubt, use the Arch Wiki. I recommend iteratively watching ahead, cross-referencing with the Arch Wiki, make a decision, and then execute.

## P.2 - Why a Virtual Machine?
I believe that using a VM for a first time installation and configuration process of a Linux distribution is (for most people) the best option. I opted to do it on [VirtualBox](https://www.virtualbox.org/) since it is very easy and lots of resources out there use this VM. Most of the information here is the same regardless of the medium but there are some notable differences in a few of the sections of pre-installation.

## P.3 - Who is this for?
This is for anyone who would like to undergo the same process I did! It is not for experienced individuals. If you would like to use `archinstall`, this post is not for you.

# Arch - My First Experience
- Arch Linux is an independently developed, x86-64 general-purpose [GNU](https://wiki.archlinux.org/title/GNU "GNU")/Linux distribution.
- Strives to provide the latest stable versions of most software.
- Follows a [rolling-release model](https://en.wikipedia.org/wiki/Rolling_release). 
- The default installation is a minimal base system, configured by the user to only add what is purposely required.

## 1 Pre-Installation
Arch Linux should run on any x86_64-compatible machine with a minimum of 512 MiB RAM, though more memory is needed to boot the live system for installation.[1](https://lists.archlinux.org/archives/list/arch-releng@lists.archlinux.org/message/D5HSGOFTPGYI6IZUEB3ZNAX4D3F3ID37/) A basic installation should take less than 2 GiB of disk space. As the installation process needs to retrieve packages from a remote repository, this guide assumes a working internet connection is available.

## 1.1 Acquire an installation image
Visit the [Download](https://archlinux.org/download/) page and, depending on how you want to boot, acquire the ISO file or a netboot image, and the respective [GnuPG](https://wiki.archlinux.org/title/GnuPG "GnuPG") signature.
- What is an ISO file?
	- An ISO file is an exact copy of an entire optical disk such as a CD, DVD, or Blu-ray archived into a single file. This file, which is also sometimes referred to as an ISO image, is a smaller sized duplicate of large sets of data.
	- Actual function is to replicate an original optical disk and store it until it is needed to burn a new disk having the same data within it.

## 1.2 Verifying
- Downloads (especially from HTTP) are generally prone to be intercepted to [serve malicious images](https://www2.cs.arizona.edu/stork/packagemanagersecurity/attacks-on-package-managers.html).
#### 1.2.1 Downloading from Mirror:
**Mirror site**: - A Web site that is a replica of an already existing site, used to reduce network traffic (hits on a server) or improve the availability of the original site. Mirror sites are useful when the original site generates too much traffic for a single server to support.
- Go to [Arch Linux Downloads](https://archlinux.org/download/#checksums).
	- Scroll to the United States mirror sites. Any of them should work. I used "constant.com" under the https protocol (_highly recommended_). To check if it's http or https, just hover the cursor over the link and it will display the URL string.
		- The ISO file you'll down will look like this: `archlinux-_version_-x86_64.iso`.
		- Under the ISO file is the ISO PGP signature which looks like: `archlinux-_version_-x86_64.iso.sig`.
		- These are the only two downloads you need.
	- Under "Checksums" there are multiple pieces of information used to check and verify the ISO file downloaded from the mirror site.
		- The ISO PGP signature is obtained from the Mirror site.
		- PGP Fingerprint.
		- SHA256 hash.
		- These ^ are the only three you need.
	- Check SHA256:
		- Open Windows PowerShell (not command prompt) and run the following command: `Get-FileHash C:\Users\YourUsername\Downloads\archlinux-2023.12.01-x86_64.iso -A SHA256`
		- This will output a hash. From there just check that it's the same as the SHA256 hash from the Arch website (I compared the strings in a .py script).
	- Verify PGP signature.
		- This requires gpg4win which you can download from their website. This will install a Kleopatra application which you will use to verify the PGP signature. You can also verify this gpg4win download.
		- In Kleopatra, if you Decrypt/Verify the signature without doing anything else, you'll get something that says 'data not verified'.
		- First import the PGP Fingerprint. Right click the imported file and click 'Certify'. From here, just input a username and click through. This certifies the public key that you imported which will be used to verify the sig file.
		- Now Decrypt/Veriy the signature and you should get a screen with a green box around the Audit log. It should say: '**Valid signature by pierre@archlinux.org'**.
		- Take a look at [This Video](https://www.youtube.com/watch?v=yJSurJ3ooL4&t=78s) if you prefer that.

## 1.3 Prepare the Installation Medium
- I am doing this through VirtualBox for now. I will update this section with information through different mediums (including different VMs, hopefully, like QEmu).
### 1.3.1 Preparing a Virtual Machine
**VirtualBox**: [This](https://www.youtube.com/watch?v=FlQ-LyBDCoo&list=PLyMERcvAKmwGbzAvJZuCi9YVrr3TbbSF_&index=1&t=240s) is the video I used. 1:05 - 5:25 are the relevant sections for this.

## 1.4 Boot the live environment
For my case (using VirtualBox), just click start on the VM for Arch and it will open some prompts to boot the live environment.

## 1.5 Set the console keyboard layout and font
- The default [console keymap](https://wiki.archlinux.org/title/Console_keymap "Console keymap") is [US](https://en.wikipedia.org/wiki/File:KB_United_States-NoAltGr.svg "wikipedia:File:KB United States-NoAltGr.svg"). Available layouts can be listed with: `localectl list-keymaps
- [Console fonts](https://wiki.archlinux.org/title/Console_fonts "Console fonts") are located in `/usr/share/kbd/consolefonts/` and can likewise be set with [setfont(8)](https://man.archlinux.org/man/setfont.8) omitting the path and file extension. For example, to use one of the largest fonts suitable for [HiDPI screens](https://wiki.archlinux.org/title/HiDPI#Linux_console_(tty) "HiDPI"), run: `setfont ter-132b`

## 1.6 Verify the Boot Mode
Odds are you are in UEFI. I'm not particularly sure about this part yet. It definitely matters and more research into this portion of the installation is needed.

## 1.7 Configure Network Connection
### 1.7.1 VM
- If you are using a VM, you don't need to do anything except verify that you have a stable connection. Use the `ping` command to do this.

## 1.8 Update the System Clock
- In the live environment [systemd-timesyncd](https://wiki.archlinux.org/title/Systemd-timesyncd "Systemd-timesyncd") is enabled by default and time will be synced automatically once a connection to the internet is established.
- Use [timedatectl(1)](https://man.archlinux.org/man/timedatectl.1) to ensure the system clock is accurate:

## 1.9 Partition the disks
**Disk partitioning** or **disk slicing** [1](https://en.wikipedia.org/wiki/Disk_partitioning#cite_note-1) is the creation of one or more regions on [secondary storage](https://en.wikipedia.org/wiki/Computer_data_storage#Secondary_storage "Computer data storage") so that each region can be managed separately [Note](https://en.wikipedia.org/wiki/Disk_partitioning#cite_note-2). 

[**Swapping**](https://wiki.archlinux.org/title/Swap): It is recommended that you read up on [paging](https://phoenixnap.com/kb/paging) and [swapping](https://www.geeksforgeeks.org/swapping-in-operating-system/) before this step if you aren't familiar or need a refresher. 
- Swapping has been around since before paging, and follows the same principle of allocating external storage space for processes and/or data that isn't as heavily needed. However, swapping isn't as fine-grained and doesn't break up the memory into smaller blocks of memory like paging does. 
- What we need to know is that [swap space](https://phoenixnap.com/kb/swap-space) in Linux is an extension of physical RAM, offering [virtual memory](https://phoenixnap.com/glossary/virtual-memory-definition) that helps maintain system stability and performance. It allows processes to continue running when RAM is fully used and prevents memory errors.
- Here is a good [supplementary resource](https://www.cs.cornell.edu/courses/cs4410/2021fa/assets/material/lecture13_memory_management_2_lightweight.pdf) on swapping and paging. 
- This is important for this step of the installation because we can make a swap partition. It isn't always *needed*, but swaps are necessary if you need the [hibernate](https://www.howtogeek.com/devops/how-to-hibernate-or-sleep-linux-from-the-command-line/) feature. It is very useful on Linux where you can forget about rebooting and shutting down. 
	- During my setup process, I didn't make swap partitions but after further research I determined that I wanted them. However, I had already ran pacstrap (Section [[Arch#2 Installation]]) and from my knowledge, if I partitioned the disk at that point I'd potentially write over existing data (such as the Linux kernel). I opted to use [Swap files](https://wiki.archlinux.org/title/swap), which are slower, but a viable option under this scenario. Details in Section --.
- Note that swapping is super slow because it does memory compaction and has to operate off a disk rather than your RAM (SSD is about 3000x slower than RAM).

**[Mounting](https://unix.stackexchange.com/questions/3192/what-is-meant-by-mounting-a-device-in-linux)**: the act of associating a storage device to a particular location in the directory tree. The most important thing to know about this other than that exact definition is just how the Linux file system works in general. File systems are tables of information corresponding to tree like structures that map to certain regions and partitions in memory.
- For example, when the system boots, a particular storage device (commonly called the root partition) is associated with the root of the directory tree, i.e., that storage device is mounted on `/` (the root directory). <--- (From the link provided on mounting.)

### 1.9.1 Virtual Machine
I haven't verified if this is the same for other VMs, but logically it should be similar since when you configure your system in your VM, you allocate memory your VM to operate off of. Most of this is exactly the same no matter how your installing Arch anyway.

- Run `lsblk` to view information of all available block devices. In our case, `sda` is the block we are operating our VM off of.
- Run `cfdisk /dev/sda` to run the partition editor to create, resize, delete, and manipulate the partitions.
- Select the `dos` type.
- Make the 'boot' partition, which will be automatically labeled as `sda1`. Make it bootable by typing `B` and you should see `BO` pop-up in the bottom of the window.
	- This partition needs about 128 MiB, but at *most* 512 MiB. If you want to be safe, you can use 512, but just know that it may not be necessary. In the future, I'll have more information on how to determine what you *really* need.
- Make another partition for everything else i.e. 'root'.
- Quit out of `cfdisk`. 

### 1.9.2 Swap File
- If you didn't make swap partitions and want to, you'll likely need to restart. However, if you are not particularly concerned about speed and efficiency for overflowing your RAM, then the [swap file](https://wiki.archlinux.org/title/swap) is a viable option.

## 1.10 Format the partitions
Now we format it using the `mkfs` command. If you created an EFI system partition, [format it](https://wiki.archlinux.org/title/EFI_system_partition#Format_the_partition "EFI system partition") to FAT32 using [mkfs.fat(8)](https://man.archlinux.org/man/mkfs.fat.8).
- **Warning:** Only format the EFI system partition if you created it during the partitioning step. If there already was an EFI system partition on disk beforehand, reformatting it can destroy the boot loaders of other installed operating systems. 
- We can format 'root' as `.ext4` but 'boot' needs to be a FAT.

Run `mkfs`...
- `mkfs.ext4 /dev/sda2` - Formats 'root' partition as `.ext4`
- `mkfs.fat -F32 /dev/sda1` - Formats the partition as a FAT with 32-bit entries.
	- Here is the Wiki [page](https://wiki.archlinux.org/title/FAT) on it. Also, here is Arch's docs on [File Allocation Tables](https://wiki.archlinux.org/title/FAT) (FAT), an essential to understanding how our OS works [(FAT isn't technically part of the OS)](https://wiki.archlinux.org/title/FAT).

Check out this Arch page on [EFI system partition](https://wiki.archlinux.org/title/EFI_system_partition) and it sort of explains why we need to format the 'boot' as a FAT and also necessary information for formatting the 'boot' partition as well as conventions for mounting this partition.

## 1.11 Mount the file systems
Now, we mount the partitions using the `mount` command.
- In order to mount our 'root' partition, we mount `/dev/sda2` to `/mnt`
	- To do this, run: `mount /dev/sda2 /mnt`
	- Note: `/mnt` is just name by tradition. You could name it anything but it is unnecessary.
- Create a directory on `/mnt` for 'boot' using the `mkdir` command.
- Mount 'boot'...
	- If your system is UEFI, then mount to `/mnt/boot/efi`.
	- If your system is EFI, then mount to `/mnt/boot`.
	- See **Section 4** in [EFI system partition](https://wiki.archlinux.org/title/EFI_system_partition) for more information on mounting.

`lsblk` to view the partitions in each block.

For a reason not entirely clear to me, after this point you will likely need to install the `efibootmgr` using `pacman -Sy`.

## 2 Installation
Now the "hard" part is done. From here, we are essentially just running [pacstrap](https://wiki.archlinux.org/title/Pacstrap). Pacstrap is designed to create a new system installation from scratch and it is mainly used during the installation of the system, and comes preinstalled within the arch installation media.
### 2.1 Select the mirrors
Packages to be installed must be downloaded from [mirror servers](https://wiki.archlinux.org/title/Mirrors "Mirrors"), which are defined in `/etc/pacman.d/mirrorlist`. On the live system, after connecting to the internet, [reflector](https://wiki.archlinux.org/title/Reflector "Reflector") updates the mirror list by choosing 20 most recently synchronized HTTPS mirrors and sorting them by download rate.

The higher a mirror is placed in the list, the more priority it is given when downloading a package. You may want to inspect the file to see if it is satisfactory. If it is not, [edit](https://wiki.archlinux.org/title/Textedit "Textedit") the file accordingly, and move the geographically closest mirrors to the top of the list, although other criteria should be taken into account.

This file will later be copied to the new system by _pacstrap_, so it is worth getting right.

### 2.2 Install essential packages
**Note:** No software or configuration (except for `/etc/pacman.d/mirrorlist`) gets carried over from the live environment to the installed system.

Use the [pacstrap(8)](https://man.archlinux.org/man/pacstrap.8) script to install the [base](https://archlinux.org/packages/?name=base) package, Linux [kernel](https://wiki.archlinux.org/title/Kernel "Kernel") and firmware for common hardware: `pacstrap -K /mnt base linux linux-firmware`
- You could omit the installation of the firmware package when installing in a virtual machine or container.
To install other packages or package groups, append the names to the _pacstrap_ command above (space separated) or use [pacman](https://wiki.archlinux.org/title/Pacman "Pacman") to [install](https://wiki.archlinux.org/title/Install "Install") them while [chrooted into the new system](https://wiki.archlinux.org/title/Installation_guide#Chroot).

See the Arch installation wiki (Section 2.2) for more details and suggestions of what packages to include in the pacstrap command.

## 3 Configure the system
### 3.1 Fstab
Arch Wiki: The [fstab(5)](https://man.archlinux.org/man/fstab.5) file can be used to define how disk partitions, various other block devices, or remote file systems should be mounted into the file system.

Your fstab file basically just contains all the drives that Linux might try to load when booting up. For more information other than the Arch Wiki on fstab, see this [link](https://linuxconfig.org/how-fstab-works-introduction-to-the-etc-fstab-file-on-linux). 

Generate an [fstab](https://wiki.archlinux.org/title/Fstab "Fstab") file (using [`genfstab`](https://wiki.archlinux.org/title/Genfstab) with`-U` or `-L` to define by [UUID](https://wiki.archlinux.org/title/UUID "UUID") or labels, respectively): `genfstab -U /mnt >> /mnt/etc/fstab`.
- Important Note: Generating the fstab without the `-U` option will have it use the device ID of your drives to identify it. This is bad because a device ID can change.
- Use the `>>` option to redirect the output to a file. E.g.: `genfstab -U /mnt >> /mnt/etc/fstab`.

Run `genfstab -U /mnt` to see what this looks like for yourself.

### 3.2 Chroot
[Chroot](https://wiki.archlinux.org/title/Chroot) stands for 'change root' and is an operation that changes the apparent root directory for the current running process and their children. A program that is run in such a modified environment cannot access files and commands outside that environmental directory tree.

Changing root is commonly done for performing system maintenance on systems where booting and/or logging in is no longer possible.

The `chroot` target should be a directory which contains a file system hierarchy (`/mnt`).

- Note: The file system that will serve as the new root (`/`) of your chroot must be accessible (i.e., decrypted, [mounted](https://wiki.archlinux.org/title/Mount "Mount")).

Run `arch-chroot` with the new root directory as first argument. 
- Change root into the new system using: `arch-chroot /mnt`

You may notice that the command prompt changes. This is because, we have changed root from our USB or virtual CD drive into our actual Arch Linux installation. Run `pwd` and it should just display root (`/`). Run `ls` and you will see the standard Linux file directories such as `bin` and `lib`.

To exit the chroot, use `exit`.

We also now have access to [pacman](https://wiki.archlinux.org/title/Pacman), the package manager in Arch.

### 3.A Using Pacman
See the [pacman](https://wiki.archlinux.org/title/Pacman) Wiki for details on pacman, it's super useful! 

Use `pacman -S` install [NetworkManager](https://wiki.archlinux.org/title/NetworkManager) and [GRUB](https://wiki.archlinux.org/title/GRUB). 

### 3.B Systemd
We want [systemd](https://wiki.archlinux.org/title/Systemd) to start the NetworkManager after boot.

To **enable** a unit to start automatically at boot, run: `systemctl enable _unit_`
- Run: `systemctl enable NetworkManager`

### 3.C GRUB
We need to configure GRUB so it knows what to boot.

Run: `grub-install /dev/sda`

Yes, `sda`. We aren't configuring GRUB on that partition, we need to configure it for the entire drive.

We then want to generate our configuration files. Use the `grub-mkconfig` tool to generate `/boot/grub/grub.cfg`. 
- Run: `grub-mkconfig /boot/grub/grub.cfg`. 
- `-o` specifies the output file as seen in [grub-mkconfig(8)](https://man.archlinux.org/man/grub-mkconfig.8).

## FAQ
### What ISA does Arch Support?
- Arch only supports the [x86_64](https://en.wikipedia.org/wiki/x86_64 "wikipedia:x86 64") (sometimes called amd64) architecture. Support for i686 was dropped in November 2017 [[1]](https://archlinux.org/news/the-end-of-i686-support/). There are _unofficial_ ports for the i686 architecture [[2]](https://archlinux32.org/) and [ARM](https://en.wikipedia.org/wiki/ARM_architecture "wikipedia:ARM architecture") CPUs [[3]](https://archlinuxarm.org/), each with their own community channels.
### Does Arch Follow the Linux Foundation's Filesystem Hierarchy Standard (FHS)
- Arch Linux follows the _file system hierarchy_ for operating systems using the [systemd](https://wiki.archlinux.org/title/Systemd "Systemd") service manager. See [file-hierarchy(7)](https://man.archlinux.org/man/file-hierarchy.7) for an explanation of each directory along with their designations. In particular, `/bin`, `/sbin`, and `/usr/sbin` are symbolic links to `/usr/bin`, and `/lib` and `/lib64` are symbolic links to `/usr/lib`.