python3 actions/volksverpetzer.py >/tmp/out.file
cat /tmp/out.file|head -c 222
grep rss /tmp/out.file -q && cp /tmp/out.file $1/volksverpetzer.xml