# Description

This repo contains all the information needed to install odoo in our outside a container.
Docker container for ubuntu 24.04 and 22.04 (docker container for Ubuntu22.04 does not support backups so try to avoid using it).
The project was deployed in Ubuntu18.04 using the medusa server. 192.168.1.160

## SETUP
Clone the repo

	git clone --recurse-submodules https://github.com/luisrlppg/PPG-ERP.git

If you want to start the docker container do:

	cd PPG-ERP/docker/dev/17/
	docker compose up -d

In case you did not used --recurse-submodules when cloning, run:

	git pull --recurse-submodules origin main

go to /main/docs/ and check odoo-install-dev.md for references for installing
odoo out of docker

check /main/docs/ and see backups.md to configure them.
