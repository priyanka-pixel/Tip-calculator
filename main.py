print("Welcome to the Tip Calculator!")
Balance = int(input("what was the total bill?\n $"))
Percentage = int(input("How much tip would you like to give? 10,12, or 15?\n"))
People = int(input("How many people to split the bill?\n"))
Tip = float((Percentage/100 * Balance + Balance))
Total= Tip/People
print(Total)