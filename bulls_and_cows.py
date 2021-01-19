import random
n =str(random.randint(1000, 10000))
print(n)
org_number = []
for i in n:
    org_number.append(i)
# print(org_number)
bulls_counter = 0

while bulls_counter < 4:
    guess_number = input("What is your guess:")
    guess = []
    for i in guess_number:
        guess.append(i)
    print(guess_number)
    # print(guess)
    cows_counter = 0
    for i in guess:
        if i in org_number:
            cows_counter += 1
    # print(cows_counter)

    if cows_counter > 0:
        if org_number[0] == guess[0]:
            bulls_counter += 1
        if org_number[1] == guess[1]:
            bulls_counter += 1
        if org_number[2] == guess[2]:
            bulls_counter += 1
        if org_number[3] == guess[3]:
            bulls_counter += 1
    counter = set(guess + org_number)
    print(counter)
    # count duplicate numbers?
    num = 0
    for x in counter:
        num += 1
    cows1 = 8 - num
    cows = cows_counter - bulls_counter
    print(str(bulls_counter)+" bulls")
    print(str(cows)+" cows")
    print(cows1)
    if bulls_counter != 4:
        bulls_counter = 0
        cows = cows_counter - bulls_counter

#     how to count duplicated values
