#!/bin/bash

# Display a dialog box with a list of installed packages, allowing multiple selection
package=$(zenity --list --title "Uninstall Package" --text "Select one or more packages to uninstall:" --column "Package" --multiple --separator "," $(dpkg --get-selections | awk '{print $1}'))

# If the user clicks "Cancel" or closes the dialog box, exit the script
if [ -z "$package" ]; then
    exit 0
fi

# Split the selected packages into an array using the specified separator character (",")
IFS="," read -ra pkg_array <<< "$package"

# Loop through the array of selected packages and uninstall them one by one
for pkg in "${pkg_array[@]}"; do
    sudo apt-get remove --purge "$pkg"
done

# Display a message to confirm that the packages have been uninstalled
zenity --info --title "Packages Uninstalled" --text "Selected packages have been successfully uninstalled."
