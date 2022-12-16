## APT-Uninstaller


This is a basic bash script written for removing unwanted installed packages from a Linux system with a user interface. To create a user interface for uninstalling packages in Linux, this script uses a tool called Zenity. Zenity is a command-line utility that allows you to display GUI dialog boxes in terminal programs.

This script will display a dialog box with a list of installed packages, and the user can select one or more packages by holding down the Ctrl key while clicking on the package names. The selected packages will be separated by commas in the output, and the script will loop through the array of selected packages, uninstalling them one by one.

To use this script, save it to a file and make it executable with the following command:

 chmod +x scriptName.sh

Then, you can run the script by typing ./scriptName.sh in the terminal.


Note that this script will only work on Debian-based systems (such as Ubuntu) that use the apt package manager. If you are using a different package manager (such as yum or dnf) or a different Linux distribution, you will need to modify the script to use the appropriate package manager commands.
