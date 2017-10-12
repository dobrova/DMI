#!/bin/bash

a=10
b=20

#piemers nr1
echo "----------------------------------------------------"


if [ $a -eq $b ]
then
echo "$a -eq $b : yes, a is equal to b"
else
echo "$a -eq $b: no, a is not equal to b"
fi

if [ $a ==  $b ]
then
echo "$a ==  $b : a is equal to b"
else
echo "$a ==  $b: a is not equal to b"
fi

echo "----------------------------------------------------"
#piemers nr2


if [ $a -ne $b ]
then
echo "$a -ne $b: yes, a is not equal to b"
else
echo "$a -ne $b : no, a is equal to b"
fi


if [ $a !=  $b ]
then
echo "$a != $b: a is not equal to b"
else
echo "$a != $b : a is equal to b"
fi

echo "----------------------------------------------------"







if [ $a -gt $b ]
then
echo "$a -gt $b: a is greater than b"
else
echo "$a -gt $b: a is greater than b"
fi

if [ $a -lt $b ]
then
echo "$a -lt $b: a is less than b"
else
echo "$a -lt $b: a is less than b"
fi



if [ $a -ge $b ]
then
echo "$a -ge $b: a is greater or equal to b"
else
echo "$a ge $b: a is not greater or equal to b"
fi

if [ $a -le $b ]
then
echo "$a -le $b: a is less or equal to b"
else
echo "$a -le $b: a is not less or equal to b"
fi

