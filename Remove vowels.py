string=input()
vow="aeiouAEIOU"
for char in string :
  if char in vow :
    string=string.replace(char,"")
    
print(string)    
