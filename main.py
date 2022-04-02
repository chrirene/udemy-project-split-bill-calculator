#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
person = input("How many people to split the bill? ")

bill_as_float = float(bill)
tip_as_int = int(tip)
person_as_int = int(person)

total = "{:.2f}".format((bill_as_float / person_as_int) * ((tip_as_int + 100) / 100), 2)
comment = f"Each person should pay: ${total}"
print(comment)



