#!/bin/bash


cmd=''

for folder in $(ls -d */ | tr ' ' '\\'); do
   f=$(echo $folder | sed --expression='s/\\/ /g')
   f="'${f::-1}'/;"
   f=$(eval echo 'tar -czvf "${f::-2}".tar.gz "${f}";')
   cmd="${cmd}${f}"
done

eval $cmd
