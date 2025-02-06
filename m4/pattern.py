# Module 4 In-Class Activity 2

height = int(input('Height: '))

for i in range(1,height+1): # from 1 - height
    print(" " * (height-i), end='')
    for j in range(1, i+1):
        print(j, end='')
    print()