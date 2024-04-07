#!/bin/bash

set -x

dockerize() {
	folder="challs/$1"
	name="dctf24.azurecr.io/challs/$2:latest"
	dockerfile=${3:-Dockerfile}
	pushd $folder
	docker build --platform=linux/amd64 -t $name -f $dockerfile . && \
	docker push $name
	popd
}

# Pwn
dockerize "library_shelves" "libraryshelves"
dockerize "librarians_revenge" "librariansrevenge"

# Rev

# Crypto
dockerize "yet_another_padding_oracle" "paddingoracle"

# Web

# Misc
