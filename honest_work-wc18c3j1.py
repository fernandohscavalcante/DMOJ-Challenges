#p = litters of paint in the bucket;
#b = litters of paint used to make a badge
#d = pokedollars

p = int(input())
b = int(input())
d = int(input())

bdgs = p//b
pntlft = p%b
profit = pntlft + (bdgs * d)
print(profit)
