print(10 * 10)
print(10 ** 10)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)
##the last answer is wrong because the actual answer is an infinitely repeating value, 0.6 forever, but it only returns up to a certain number of decimal places.

rate = float(input("Please input the current exchange rate for the Euro to the US Dollar: "))
amount = int(input("Thank you. Please input how many Euros you would like to exchange: "))
total = (amount*rate)
result = (total-3)
print("We have charged a processing fee of $3.00 for your transaction. Your total is", f"${result}.", "Thank you for using our service!")
