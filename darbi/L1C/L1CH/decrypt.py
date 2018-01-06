fmeta = open("meta2.bin", "rb")                      # atvert failu meta2.bin lasīšanai
fmeta.seek(0)                                        # kursors failā tiek novietots uz faila sākumu

fdata = open("data2.bin", "rb")                      # atvert failu data2.bin lasīšanai
fdata.seek(0)                                        # kursors failā tiek novietots uz faila sakumu

poz = 0                                              # definē mainīgo kurš norādis uz vajadzīgā baita pozīciju   
odd = bool(True)                                     # definē mainīgo kurš norādīs ciklā vai nu uz nobīdi vai nu masku 

while 1:                                              
	b = fmeta.read(1)                            # nolasa vienu baitu -> 'b'
	if not b:                                    # ja baits nav nolasams -nav ko lasīt
		break                                # partraucam lasīsanu  
	if odd:                                      
		poz = poz + ord(b)                   # poz tiek pieskatita mainīga b vertiba  
		fdata.seek(poz)                      # data2.bin kursors parvietojas uz poziciju atbilstošu 
		x = fdata.read(1)                    # definējam mainīgo kas atbilst viena baita nolasīšanai
		odd= not odd                         # pieškiram mainīgam invērso vērtibu (true->false vai false-true)
	else:
#		print hex(ord(b)), " ", hex(ord(x))  # bija uztaisīts pārbaudei hex sistemā 
#		print bin(ord(b)), " ", bin(ord(x))  # bija uztaisīts parbaudei bin sistēmā
		print chr(ord(b)^ord(x))             # attēlojam baitu kas iegūts  (b)^OR(x) simbola veidā      
		odd= not odd                         # piešķiram mainigam invērso vērtibu
#	print "\n"                                   # bija uztaisīts parbaudei  
fmeta.close()                                        # aizveram failu meta2.bin
fdata.close()                                        # aizveram failu data2.bin

