print("Welcome to GC Fruit Market!")
name = input("What is your name? ")
fruit_options = ["Apple $2", "Grape $1", "Orange $3"]
# Infinite loop
apple_count = 0
grape_count = 0
orange_count = 0
more_fruit = str('y')
while 'y':
    print(f"Welcome {name}. Which fruit would you like to buy?")
    print(f"1. {fruit_options[0]}")
    print(f"2. {fruit_options[1]}")
    print(f"3. {fruit_options[2]}")
    fruit_type = int(input("> "))
    if fruit_type == 1:
        print("You bought 1 apple at $2")
        apple_count += 1
    elif fruit_type == 2:
        print("You bought 1 grape at $1")
        grape_count += 1
    elif fruit_type == 3:
        print("You bought 1 orange at $3")
        orange_count += 1
    print("Would you like to buy another piece of fruit? y/n ")
    more_fruit = input('> ')
    if more_fruit != 'y':
        break
print(f"Order for {name}")
print(f"{apple_count} apple(s) at $2 apiece")
print(f"{grape_count} grape(s( at $1 apiece")
print(f"{orange_count} orange(s) at $3 apiece")
sub_total = (apple_count * 2) + (grape_count * 1) + (orange_count * 3)
print(f"Sub Total: ${sub_total}")
tax = sub_total * 0.05
print(f"5% Tax: ${tax}")
total = tax + sub_total
print(f"Total: ${total}")
