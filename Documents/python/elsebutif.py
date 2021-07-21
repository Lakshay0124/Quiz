

a=int(input("Enter Your Marks Of English - "))
b=int(input("Enter Your Marks Of Maths   - "))
c=int(input("Enter Your Marks Of Science - "))
d=int(input("Enter Your Marks Of Sst - "))
e=int(input("Enter Your Marks Of Hindi - "))
if (a>33):
    print("Pass In English")
else:print("Fail In English")
if (b>33):
        print("Pass In Maths")
else:print("Fail In Maths")  
if (c>33):
         print("Pass In science")
else:print("Fail In Science")
if (d>33):
         print("Pass In Sst")
else:print("Fail In Sst")
if (e>33):
            print("Pass In Hindi")
else:print("Fail In Hindi")

if (a<33 or b<33 or c<33 or d<33 or e<33):
    print("Over all result - \n You are failed")
else:print("Over all result - \n Congras You Passed !")
