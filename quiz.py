score=0
print("Welcome TO Quiz Game")
print("Caution:Give answer in Lowercase only")

    
d1=input("Who invented the Light Bulb? - ")
if (d1=="thomas alva edison"):
        print("Correct!")
        score += 1
else:
    print("Wrong!")
    

d2=input("Which country has the largest population in the world? - ")
if (d2=="china"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
d3=input("CPU Stands For - ")
if  (d3=="central processing unit"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
d4=input("Who Wrote Harry Potter - ")
if  (d4=="jk rowling"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
d5=input("76x5+45-6= ")
if (d5=="419"):
    print("Correct!")
    score += 1

else:
    print("Wrong!")
    
d6=input("What Does BBC Stands For - ")
if (d6=="british broadcasting corporation"):
    print("Correct!")
    score += 1

else:
    print("Wrong!")
    
d7=input("What Is The National Currency Of Russia - ")
if  (d7=="ruble"):
    print("Correct!") 
    score += 1
else:
    print("Wrong!")
    
d8=input("The Long Term Assets Which Don't Have Any Physical Existence But are rights That Have Value is Known As- ")
if  (d8=="intangible assets"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")

d9=input("What is Full Form of ISRO - ")
if  (d9=="indian space research organisation"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
d10=input("which is most spoken language in the world - ")
if  (d10=="english"):
    print("Correct!")
    score += 1
else:
    print("Wrong!")
    
print("Your Final Score Out Of 10 Is - ",score)
