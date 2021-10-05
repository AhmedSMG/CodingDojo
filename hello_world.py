
# 1
print("Hello World")

# 2 
username = input("Enter username: ")
# a
print("Hello", username)
# b
print("Hello " +  username)

# 3
usernumber = int(input("Enter number: "))
# a
print("Hello", usernumber)
# b
print("Hello " + str(usernumber))

# 4
food_one, food_two = input("Enter your two favorite foods: ").split(",")
# a
print("I love to eat {one} and {two}".format(one=food_one, two=food_two))
# b
print(f"I love to eat {food_one} and {food_two}")
