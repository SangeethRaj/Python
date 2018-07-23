a=list("string")
b=list("strng")
c=0
for i in a:
    if i in b:
        c+=1;
print (len(b));
if len(a) > len(b):
    if c == len(a):
        print ("yes");
elif len(a)<len(b):
    if c==len(b):
        print ("yes");
else:
    print("no");
