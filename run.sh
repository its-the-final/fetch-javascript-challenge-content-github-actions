#!/bin/bash
startdir=$(pwd)
mkdir public

for file in actions/*.sh;
do  bash "$file" $startdir/public;done
exit 0
