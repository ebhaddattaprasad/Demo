"""
a=[1,2,3,4,5,6]
b=[2,3,4,5,6]
o/p
if a[3] and b[3] is same print both are equal
"""
a=input()
b=input()
a_final=a.split()
b_final=b.split()

if a[3]==b[3]:
    print("3rd value of a {} is same as 3rd value of b {}".format(a[2],b[2]))
else:
    print("3rd value of a {} is not same as 3rd value of b {}".format(a[2],b[2]))