email=input("Enter your email: ")
em=email.strip()
# print(em)
parsed=em.split('@')
username=parsed[0]
domain_part=parsed[1]
if '.' in domain_part:
    domain_name=domain_part.split('.')[0]
else:
    domain_name=domain_part

print(" User Name:",username,"\n","Domain Name: ",domain_name, "\n")
