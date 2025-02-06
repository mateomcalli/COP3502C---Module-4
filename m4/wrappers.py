# Module 4 In-Class Activity 3

money = int(input('How much money do you have: '))

bars = money // 4
while money % 3 == 0:
    bars += 1

print(f'You can purchase {bars}')