#!/bin/bash

echo "" > report2.log
arr=()
count=0
while true
do
	arr+=(1 2 3 4 5 6 7 8 9 10)
	((count++))
	if [[ $count -eq 100000 ]]
	then
		count=0
		echo "${#arr[@]}" >> report2.log
	fi
done

