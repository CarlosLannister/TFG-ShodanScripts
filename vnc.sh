#!/bin/bash
for ip in ‘cat IPshot.csv‘; do
	echo $ip
	timeout 180 xwd -root -display $ip:0 | convert xwd:- /tmp/screen-$ip.png
done