amount = float(input ("What is your deposit amount?  "))
years = int(input ("For how many years you want to deposit? "))
i = 0
interest = 0
for year in range(0, years): 
	interest = (amount / 100) * 10
	amount = amount + interest
	i = i + 1

print("Your deposit in " + str(years) + " years will become "+ str(amount))
