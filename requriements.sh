#!/bin/sh
#install all requirement for arch/debian/fedora for my script to work
sudo apt update && sudo apt full-upgrade && sudo apt autoremove && sudo apt install wget  python3
sudo pacman -Syyu wget python3 python3-pip pipx
sudo dnf update && sudo dnf clean all && sudo dnf install wget python3

#credit the Author
echo "script By TigerClips1"
echo "ps4linux.com"
echo "https://ko-fi.com/tigerclips1"
echo "https://twitter.com/TugerClips1"