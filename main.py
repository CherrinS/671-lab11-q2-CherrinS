# YOUR CODE HERE
n=int(input())
lst1=[]
lst2=[]
updated_list=[]
for i in range(n):
    l1=int(input())
    lst1.append(l1)
for i in range(n):
    l2=int(input())
    lst2.append(l2)

def summation(lst1,lst2):
    for j in range (n):
        a=lst1[j]+lst2[j]
        updated_list.append(a)
    return(updated_list)
result=summation(lst1,lst2)
print(result)

def find_min_max():
    minnie=min(updated_list)
    maxy=max(updated_list)
    return minnie,maxy
result=find_min_max()
print(result)
