import math
import csv

with open('stdev.csv', newline='') as f:
        reader = csv.reader(f)
        file_data = list(reader)

data = file_data[0]


## calculating mean...

n = len(data)
total = 0

def mean(data): 
        n= len(data) 
        total =0 
        for x in data: 
                total += int(x) 

        mean = total / n 
        return mean


## now subtracting mean from total and squaring it...

sqr_list = []

for x in data:
        a = int(x)-mean(data)
        a = a ** 2
        sqr_list.append(a)

sum = 0

for i in sqr_list:
        sum = sum+i

result = sum/n

## finally, taking the square root of this value

sqrt = math.sqrt(result)

print(f"standard deviation is {sqrt}")




