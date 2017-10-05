#!/bin/bash

echo "--------------------------------"
#6. piemers - logisjkas operacijas
if [ $# == 2 ]
then
echo "--------------------------------"
#5. piemers  (+,-,*,/) ar argumentiem
a=$1
b=$2
val51=`expr $a + $b`
echo "$a + $b = "$val51
val52=`expr $a - $b`
echo "$a - $b = "$val52
fi

echo "--------------------------------"
#4. piemers  (+,-,*,/) ar mainigajiem
a=10
b=30
val41=`expr $a + $b`
echo "$a + $b = "$val41
val42=`expr $a - $b`
echo "$a - $b = "$val42

echo "--------------------------------"
#3 piemers (+,-,*./)
val31=`expr 2 + 3`
echo "2+3 = " $val31
val32=`expr 2 \* 3`
echo "2 * 3 = " $val32
val33=`expr 2 / 3`
echo "2 / 3 = " $val33 

echo "--------------------------------"
#2. piemers merkis 2+2=4
echo "Neparasti" $val1
val2='expr 2 + 2'
echo "neparastie" $val2
val3=`expr 2 + 2`
echo "Total value : $val"

echo "--------------------------------"
#1. pemers (merkis 2+2 sasniegt 4)-gala rezultats ir simbolu rinda nevis 4!!!
val=`expr 2 + 2`
echo "--------------------------------"
