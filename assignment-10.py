#Q-1.
import re
i=0
email=input("enter email")
x=re.finditer("^[a-zA-Z0-9][_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com|rediffmail.com)$",email)
for m in x:
    i=m.group()
if email==i:
    print("valid email")
else:
    print("invalid email")


    
#Q-2.
import re
i=0
n=input("enter number")
z=re.finditer("^[6-9]{1}[0-9]{9}",n)
for m in z:
    i=m.group()
if n==i:
    print("indian number")
else:
    print("not an indian number")
