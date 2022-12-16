#!/bin/bash

# Store the details of all installed packages in a file called "installed-packages.txt"
#  dpkg -l | awk '{print $2, $3, $4, $5}' > installed-packages.txt

dpkg -l | column -s $'\t' -t -c 20 > installed-packages.txt
