#!/bin/bash
declare -i count=0

while [[ 1 ]]; do
	echo "Press 1 : To search and modify all texts"
	echo "Press 2 : To change the size (scale)"
	echo "Press 3 : To change the size in centimetres (width and heigth input)"
	echo "Press 4 : To change the position of Legend Box "
	echo "Press 5 : To Exit"
	read a
	echo "You pressed "$a
	if [[ $a == "1" ]]; then
		echo "TEXT EDITING(Shifting)"
		if [[ $count == 0 ]]; then
			python3 move.py $1 $2
		else
			python3 move.py $2 $2
		fi
		count=`expr $count + 1`
	elif [[ $a == "2" ]]; then
		echo "SCALING"
		if [[ $count == 0 ]]; then
			python3 scale1.py $1 $2
		else
			python3 scale1.py $2 $2
		fi
		count=`expr $count + 1`
	elif [[ $a == "3" ]]; then
		echo "SCALING With CENTIMETRES DIMENSIONS"
		if [[ $count == 0 ]]; then
			python3 scale2.py $1 $2
		else
			python3 scale2.py $2 $2
		fi
		count=`expr $count + 1`
	elif [[ $a == "4" ]]; then
		echo "SHIFTING LEGEND BOX"
		if [[ $count == 0 ]]; then
			python3 legend.py $1 $2
		else
			python3 legend.py $2 $2
		fi
		count=`expr $count + 1`
	elif [[ $a == "5" ]]; then
		echo "Exitting : ThankYou for using"
		break
	else
		echo "Wrong input try again"
	fi
done
