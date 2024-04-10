#!/bin/bash

set -x

az acr login -n dctf24

dockerize() {
	folder="challs/$1"
	name="dctf24.azurecr.io/challs/$2:latest"
	dockerfile=${3:-Dockerfile}
	extra=${4:-""}
	pushd $folder
	docker build --platform=linux/amd64 -t $name -f $dockerfile $extra . && docker push $name
	popd
}

dockerize "integer" "integer"
dockerize "adminlogin" "adminlogin"
dockerize "pwn-gambler" "gambler"
dockerize "librarians_revenge" "librariansrevenge"
dockerize "yet_another_padding_oracle" "paddingoracle"

dockerize "pack_the_flag" "packtheflag"
dockerize "glasbenik/chall" "musix"
dockerize "back-me-up/chall" "backmeup"
dockerize "i7n" "i7n" "Dockerfile" "--build-arg FLAG=dctf{formerly_known_as_x}"
