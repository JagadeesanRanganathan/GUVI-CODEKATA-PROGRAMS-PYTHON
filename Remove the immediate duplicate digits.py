s=input()
res=""
for i in range(len(s)):
    if(i==0 or s[i]!=s[i-1])and(i==len(s)-1 or s[i]!=s[i+1]):
        res+=s[i]
if len(res)==0:
    print(-1)
else:
    print(res)