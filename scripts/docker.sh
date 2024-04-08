#!/bin/bash

set -x

az acr login -n dctf24

dockerize() {
	folder="challs/$1"
	name="dctf24.azurecr.io/challs/$2:latest"
	dockerfile=${3:-Dockerfile}
	pushd $folder
	docker build --platform=linux/amd64 -t $name -f $dockerfile . && docker push $name
	popd
}

dockerize "integer" "integer"
dockerize "adminlogin" "adminlogin"
dockerize "pwn-gambler" "gambler"
dockerize "librarians_revenge" "librariansrevenge"
dockerize "yet_another_padding_oracle" "paddingoracle"

dockerize "glasbenik/chall" "musix"
