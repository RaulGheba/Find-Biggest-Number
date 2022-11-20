
list=[14,25,145,24,39,45,5,240]

endOfList=False
 
start=input("start")
if start=="yes":
  
 while not endOfList:
  newValue=0
  for i in range(0,len(list)):
   value=list[i]
   if i==len(list)-1 and value>newValue: #IF ITS THE LAST NUMBER
     newValue=list[i]
     
   elif value>list[i-1] and value>list[i+1] and i<len(list)-1 and value>newValue:
    newValue=value
  if i==len(list)-1 and endOfList==False:
    print(newValue)
    endOfList=True
  


