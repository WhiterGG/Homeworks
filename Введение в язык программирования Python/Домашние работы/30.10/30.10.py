count = 0
summa = 0
max = 0
min = 0

while True:
    number = int(input())
    
    if number == 0:
        break
    
    count += 1
    summa += number
    
    if number > max:
        max = number
        
    if number < min:
        min = number
    
print(count, summa, max, min)