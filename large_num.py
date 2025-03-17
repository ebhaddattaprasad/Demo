a=[10,5,61,3,5,9,11]
b=[]
large=0
for item in a:
    if item >=large:
        large=item
print(f"large number is {large}")