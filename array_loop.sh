#!/bin/bash
array=( "$@" )
N=$#
#echo array
#echo ${array[0]}
#echo ${array[1]}





k=0
while (( $k < $N ))
do
	echo "Masiva $k. elements ir vienads ar ${array[$k]} "
	k=`expr $k + 1`
done




: <<'END'
a=$1
b=$2
c=$3
END
