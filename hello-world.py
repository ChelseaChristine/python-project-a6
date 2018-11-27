print("Hello World!")

#creating variables

x = 5
y = "John "

print(x)

#this is how you leave a comment without it effecting the programming

#This is a tip calculator that asks for user input in order to calculate the
#correct tax and tip

price= float(input("What is the cost of your meal?(in the form of 00.00): "))
tax= 6.75/100
tip= 15.0/100
price=price + tax*price
total=price + tip*price

print("Your total, including tax and tip, is: " , total)
