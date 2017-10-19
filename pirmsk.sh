#!/bin/bash

numberz () {
for i in {2..100..1}
do
      for j in {2..50..1}
      do
             if [ $i -ne $j -a `expr $i % $j` -eq 0 ]
            	 then 
                   success=0; break
		else	
			success=1
	fi
done 
	if [ $success -eq 1 ]
	then
     printf "$i \n"; success=0
fi
done
}
numberz
