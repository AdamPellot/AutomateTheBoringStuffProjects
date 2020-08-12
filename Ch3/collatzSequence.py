#! python3
# collatzSequence.py - Keeps producing the collatz sequence until the
#                      result is 1.
# Adam Pellot


# Produces the collatz sequence.
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

# Keeps prompting user for a number to input into the sequence until
# the result is one.
while True:
    number = input()
    try:
        number = int(number)
    except ValueError:
        print("Enter a number")
        continue
    value = collatz(number)
    if value == 1:
        break
