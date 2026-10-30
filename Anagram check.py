s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
if (len(s1)!=len(s2)):
  print("false")
elif sorted(s1)==sorted(s2):
  print("true")
else:
  print("false")
  
  

