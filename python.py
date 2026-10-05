# question 1
print("Hello World....by Gitanjali")

# question 2
Cost_price = float(input("Cost Price:  "))
Selling_price = float(input("Selling Price:  "))
if Selling_price > Cost_price:
    profit = Selling_price - Cost_price
    print("Profit:", profit)
elif Selling_price < Cost_price:
    loss = Cost_price - Selling_price
    print("Loss:", loss)
else:
    print("No Profit No Loss")


# Question 3
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is the even number.")
else:
    print(f"{num} is the odd number.")

    # Question 4
age = int(input("Enter your age: "))
if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Valid age. You are eligible for voting")
else:
    print("Valid age, but you are not eligible for voting")

    #question 5
word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
if sorted(word1) == sorted(word2):
    print(word1, "and", word2, "are Anagrams")
else:
    print(word1, "and", word2, "are Not Anagrams")
