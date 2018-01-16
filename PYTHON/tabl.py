skaitlis=input("Ievadiet skaitli: ")
print "\nsk\t%1\t%2\t%3\t%4\t%5\n"

for x in range(skaitlis, skaitlis+11, 1):
	print "%d \t"%(x),
	for i in range(1, 6, 1):
		sk_mod=x%i
		print "%d \t"%(sk_mod),
	print "\n" 
