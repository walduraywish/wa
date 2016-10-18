total = 0

with open('num.txt', "r") as inp:
   for line in inp:
       try:
           num = float(line)
           total += num
    
       except ValueError:
           print('{} is not a number!'.format(line))

print('average of the numbers: {}'.format(total/2))
