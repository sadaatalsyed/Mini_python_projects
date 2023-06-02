
def find_max(lst):
    maximum=0
    for i in range(len(lst)):
        # print(lst[i]*2)
        if lst[i]>maximum:
            maximum=lst[i]
    return maximum

def LCM(lst):
    
    greatest=find_max(lst)
    while (True):
        tag=0
        for i in range(len(lst)):
            
            if(greatest % lst[i]==0):
                # print(f"test {i} passed")
                tag+=1
        if tag==len(lst):
            # print(tag)
            lcm=greatest
            break
        greatest+=1
    
    
    return lcm

# print(LCM(num1,num2))
# print(LCM(num_list))

listn=input("Enter comma seperated list:\t")
list1=listn.split(',')
u_list=[]
for i in range(len(list1)):
    u_list.append(int(list1[i]))
print("Your entered list: ",u_list)
print("LCM: ",LCM(u_list))