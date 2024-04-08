#!/bin/bash

FAKE_FLAG="dctf{test_flag}"

script_path=$(dirname $(realpath $0))
tempdir=$(mktemp -d)
echo "Tempdir $tempdir" >&2

## Create file list
pushd ./chall
file_list=$(git ls-files --cached --others --exclude-standard | grep -v -e prettierrc)
echo -e "Files:\n===\n$file_list\n===" >&2
popd

cp -r chall/* chall/.* $tempdir

## Change stuff

# # Find flag file in tempdir
# flagfile=$(find $tempdir -name flag.txt)
# [ -z "$flagfile" ] && echo "Flag file not found" >&2 && exit 1
# [ $(echo $flagfile | wc -l) -gt 1 ] && echo "Multiple flag files found" >&2 && exit 1
# echo "Overriding flag file $flagfile" >&2
# echo $FAKE_FLAG > $flagfile

# Sed all occurances in files
for file in $file_list; do
    echo "Sedding $file" >&2
    sed -i "s/dctf{.*}/$FAKE_FLAG/g" $tempdir/$file
done

pushd $tempdir
tar -czf $script_path/dist.tar.gz -C $tempdir $file_list
popd

rm -rf $tempdir
