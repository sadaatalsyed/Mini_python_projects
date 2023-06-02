
def find_min(lst):
    minimum=lst[0]
    for i in range(len(lst)):
        # print(lst[i]*2)
        if lst[i]<minimum:
            minimum=lst[i]
            print("Minimum:",minimum)
    return minimum

def HCF(lst):
    
    smallest=find_min(lst)
    while (True):
        tag=0
        for i in range(len(lst)):
            
            if(lst[i] % smallest==0):
                # print(f"test {i} passed")
                tag+=1
        if tag==len(lst):
            # print(tag)
            hcf=smallest
            break
        smallest-=1
    
    
    return hcf


listn=input("Enter comma seperated list:\t")
list1=listn.split(',')
u_list=[]
for i in range(len(list1)):
    u_list.append(int(list1[i]))
print("Your entered list: ",u_list)
print("HCF: ",HCF(u_list))