#!/bin/bash
docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome
sleep 10
startdir=$(pwd)
mkdir public
echo "nothing here" > public/index.html
for file in actions/*.sh;
do  bash "$file" $startdir/public;done
exit 0
