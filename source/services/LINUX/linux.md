# Linux Basics

Linux is the basis of a lot of different operating systems. Many companies and developers release their own versions of linux called distributions or distros.
The biggest companies being RedHat (RedHat Enterprise Linux) and Canonical (Ubuntu).

## Linux basics cheat sheet

### Basic commands

Some symbols have special meanings in the terminal:
- `/` refers to the root directory
- `.` refers to your current working directory
- `~` refers to the current users home directory

| **Command**                   | **What it does**                                                                                     |
| ----------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Navigate the filesystem**   |                                                                                                      |
| ls                            | Lists the files in your current working directory                                                    |
| cd \<path or directory\>      | Move through the file system using either relative or absolute paths. `cd ..` to go up one directory |
| pwd                           | Prints your current working directory                                                                |
| **File manipulation**         |                                                                                                      |
| cp \<src\> \<dest\>           | Copies files or directories                                                                          |
| mv \<src\> \<dest\>           | Moves files or directories                                                                           |
| rm [-r] \<file or directory\> | Deletes files (add -r to delete recursively)                                                         |
| cat \<filename\>              | Print out the contents of a file                                                                     |
| less \<filename\>             | Prints out the contents of a file but with the ability to scroll and search by typing /. Quit with q |
| nano \<filename\>             | Is a basic and easy to use text editor                                                               |
| mkdir \<directoryname\>       | Creates a new directory                                                                              |
| touch \<filename\>            | Creates a new empty file                                                                             |
| **Miscellaneous**             |                                                                                                      |
| sudo \<command\>              | Gives the user admin privileges for the command                                                      |
| man \<command\>               | Opens a manual for the given command                                                                 |
| history                       | Prints previously entered commands                                                                   |
 
### Managing packages

Different distros use different tools to manage packages called package managers.\n
I will use `nano` as an example package:\n
Nano is a popular and very easy to use terminal text editor.\n
Other examples would be Vim or Emacs but those aren't as beginner friendly\n
Debian and distros based on it  use `apt`:
```bash
sudo apt update && sudo apt upgrade     # updates the system
apt search nano                         # search for nano in repositories
sudo apt install nano                   # installs nano
sudo apt remove nano                    # to remove the package
```

RedHat based distros like Almalinux use `dnf`:
```bash
sudo dnf update         # updates the system
dnf search nano         # search for nano in the repositories
sudo dnf install nano   # installs nano
sudo dnf remove nano    # to remove the package
```

## Users

### Creating a new user

The command used to create a new user is called `useradd`.

Just by running `useradd your_user` a new user named your_user will be created, but you probably want to add some parameters.
The options of the `useradd` command are:
- `-m` This will create a home directory in `/home/your_user`
- `-G group_name` will add the newly created user to the here specified groups (`wheel` is an often used group since it allows the user to use `sudo`)
- `-s path/to/shell` changes the default shell of the user. The available shells and their paths can be checked with `cat /etc/shells`. If the shell you want to use is not available it can be installed using the OSs package manager.

### Modifying an existing user

In case you forgot to set something when creating the user, you can do that afterwards using the `usermod` command.

- `-aG` to add another group to a user
- `-s` to change the users default shell

For any additional options you might want to know you can always check the man pages using `man usermod` or any other command.


### How to add an SSH key to a user?

This guide shows how to add an SSH key to an existing user with a home directory.
The SSH daemon queries the .ssh/authorized_keys file and checks the content of this file against the provided private key.

If you are the responsible person of a project, and you don't have access to an EODC VM please send your public key to support@eodc.eu and we will add the key for you.

You have to use the file with the `.pub` extension. The other key without a file extension is your private key and should never be shared with anybody. The private key is easily recognized by its beginning: 
`-----BEGIN OPENSSH PRIVATE KEY-----`


```bash
[remote_user@eodc ~]$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCmqcvQgmx6mPuhOsp...oC0oy1oiCRTcCNU4TWKwdpWEzxw== your_email@example.com" >> ~/.ssh/authorized_keys  
[remote_user@eodc ~]$ cat .ssh/authorized_keys    
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCmqcvQgmx6mPuhOsp...oC0oy1oiCRTcCNU4TWKwdpWEzxw== your_email@example.com
[remote_user@eodc ~]$ chmod 0600 ~/.ssh/authorized_keys
```


## Groups


You can check the manual of the ``groupadd`` command in the terminal with `man groupadd`.

This article goes hand in hand with the User Creation Article.

Typically, a dedicated group is required for read and write access to your private EO-Storage. We will provide you a group ID in our welcome e-mail. After creating a VM, you will need to create the group separtely on each VM. Afterwards all users that shall have access to your private EO-Storage must be added to the group. 


### Create a group
To create a group, use the `groupadd` command:
`groupadd -g GROUP_ID group_name`

Example using group ID 5000:
`groupadd -g 5000 group_name`

### Add a user to the group
Often used flags are `-a` (append) and `-G` (group).
This tells `usermod` we are appending to the group name that follows the option.

```bash
ubuntu@eodc:~$ sudo usermod -aG sudo your_user
ubuntu@eodc:~$ sudo usermod -aG group2,group3,group4 your_user
```

You can check the user groups with the `id` command

```bash
ubuntu@eodc:~$ id your_user
```
