a=list("string");
for i in range(0,len(a)):
    if (i%2==0) and ((i+1)%2!=0):
        temp=a[i];
        a[i]=a[i+1];
        a[i+1]=temp;
        
    res="".join(a)
    print res
