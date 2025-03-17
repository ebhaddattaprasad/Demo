start_value=0
next_value=1
list1=[start_value,next_value]
i=0
j=1
k=2
add=0
add1=0
count=0
loop=6
add=list1[i]+list1[j]
list1.append(add)
while count<=loop:
   add1=list1[j]+list1[k]
   list1.append(add1)
   count +=1
   j +=1
   k +=1
print(list1)
print("First commit")


