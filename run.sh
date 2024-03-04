#!/bin/bash
startdir=$(pwd)
mkdir public
echo "nothing here" > public/index.html
for file in actions/*.sh;
do  bash "$file" $startdir/public;done
exit 0
