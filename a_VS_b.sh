#!/bin/bash

echo "Cienijamais lietotaj,ludzu, ievadi pirmo skaitli"
read a
echo "Cienijamais lietotaj,ludzu, ievadi otro skaitli"
read b
echo "Cienijamais lietotaj,ludzu, ievadi treso skaitli"
read c

if (( $a > $b && $a > $c ))
then
echo "a ($a) - lielakais skaitlis "
elif (( $b > $a && $b > $c ))
then
echo "b ($b) - lielakais skaitlis "
elif (( $c > $b && $c > $a ))
then
echo "c ($c) - lielakais skaitlis "
fi






: <<'END'
echo "Cienijamais lietotaj,ludzu, ievadi pirmo skaitli"
read a
echo "Cienijamais lietotaj,ludzu, ievadi otro skaitli"
read b

if (( $a == $b ))
then
echo "a ($a) ir vienads ar b ($b)"
elif  (( $a > $b ))
then
echo " ($a) > ($b)"
else
echo " ($a) < ($b)"
fi  
END






: <<'END'
if [ $a -eq $b ]
then
echo "a ($a) ir vienads ar b ($b)"
fi

if [ $a -gt $b ]
then
echo " ($a) > ($b)"
fi

if [ $a -lt $b ]
then
echo "($a) < ($b)"
fi  
END



