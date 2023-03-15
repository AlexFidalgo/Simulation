import random

n = 100000
count = 0

for i in range(n):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        count += 1

pi_estimate = 4*count/n # count/n = pi*r^2/4 = >pi = count*4/n
print(pi_estimate)

