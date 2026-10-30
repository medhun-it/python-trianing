s=input()
vowelcount=0
con=0
for i in s:
  if i in "aeiouAEIOU":
    vowelcount = vowelcount+1 
  else:
    con=con+1 
    
print(vowelcount)
print(con)
    
