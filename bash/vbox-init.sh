#!/bin/bash

RUNNING="\e[35m"
FAILED="\e[1;31m"
END="\e[0m"

paquetes=("git" "vim" "smbclient" "virtualbox-guest-utils" "xf86-video-vmware" "linux-headers" "linux-lts-headers" "linux-lts")

function main() {

	echo -e "$RUNNING Initializing system... $END"
	sudo pacman -S --noconfirm ${paquetes[@]} || echo -e "$FAILED System initialization failed$END"

	echo -e "$RUNNING Cloning dotfiles... $END"
	git clone https://github.com/druxorey/dotfiles.git ~/dotfiles || echo -e "$FAILED Cloning failed$END"

	echo -e "$RUNNING Setting aliases... $END"
	echo -e "Enter the server's ip: "
	read ipServer
	echo "Enter the server's username: "
	read usernameServer
	echo "Enter the server's password: "
	read passwordServer

	echo "alias buho='smbclient //$ipServer -U $usernameServer%$passwordServer'" >> .bashrc
}

main $@
