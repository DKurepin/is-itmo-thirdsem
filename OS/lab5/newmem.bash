#!/bin/bash

N=$1
arr=()

while true
do
	arr+=(1 2 3 4 5 6 7 8 9 10)
	if [[ ${#arr[@]} -gt $N ]]
	then
		echo "done"
		exit 0
	fi
done

