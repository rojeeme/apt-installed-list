#!/bin/bash

# Store the details of all installed packages in a file called "installed-packages.txt"
#  dpkg -l | awk '{print $2, $3, $4, $5}' > installed-packages.txt

dpkg -l | column -s $'\t' -t -c 20 > installed-packages.txt


# Display the contents of a text file in a dialog box


# Check if the file exists
if [ ! -f "installed-packages.txt" ]; then
  # If the file doesn't exist, display an error message
  yad --error --text "File not found: installed-packages.txt"
  exit 1
fi

# Display the contents of the file in a dialog box
cat "installed-packages.txt" | yad --text-info --title "installed-packages.txt" --width=600 --height=400

