
#!/bin/bash
#if (...) then ... elif () then ... else ... fi
a=$1
if (( $a > 0 )); then
	echo "Izdruka  no gaklvena zara.(ja gadijuma)tad, kad $a>0"
elif (( $a == 0 )); then
        echo "Alt.zars (ja gad.) tad kad $a ir >1" 
else
	echo "Galv zara (visi atlikusie gad.)"
	echo "vai viennozimigs ne visiem iepr.jautajumiem"
fi
echo "Izdruka jebkura gadijuma"



: <<'END'
#if (...)then ... fi
a=$1
if (( $a > 0 ))
then
	echo "Izdruka  no gaklvena zara.(ja gadijuma)tad, kad $a>0"
fi
echo "Izdruka jebkura gadijuma"




#if (...)then ... fi
a=$1
if (( $a > 0 ))
then
	echo "Izdruka  no gaklvena zara.(ja gadijuma)tad, kad $a>0"
else
	echo "Izdruka  no gaklvena zara.(ja gadijuma)tad, kad $a<0"
fi
echo "Izdruka jebkura gadijuma"

END
