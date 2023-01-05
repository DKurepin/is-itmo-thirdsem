#!/bin/bash

n=$1
k=$2
for (( i = 0; i < $k; i++ ))
do
	./newmem.bash $n &
	sleep 1
done

