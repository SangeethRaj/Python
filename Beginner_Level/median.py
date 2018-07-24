a=['4','2','3','6'];
n = len(a)
if n%2==1:
    print sorted(a)[n//2];
else:
    sum(sorted(a)[n//2-1:n//2+1])/2.0
