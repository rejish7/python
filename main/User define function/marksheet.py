# inpu the marksheet of the student

def marksheet():
       
       Name = input("Enter your Name :")
       Eng = int(input ("Enter English Marks :")) 
       Mat = int(input ("Enter Maths Marks :"))
       Sci = int(input ("Enter Science Marks :"))
       Soc = int(input ("Enter Social Marks:"))
       Nep = int (input("Enter Nepali marks :"))    
       total = Nep+Eng+Mat+Sci+Soc
       per = total/5
       
       grade = ""
       if per>35 and per<=45:
            grade="C"
       elif per>45 and per<=60:
            grade="B"
       elif per>60 and per<=75:
         grade="A"
       elif per>75 and per<=100:
            grade="A+"
       else:
            grade="Fail"
       
       print("------------------------------")
       print("         Marksheet            ")
       print("------------------------------")
       print(f"Name: {Name}") 
       print(f"English Marks: {Eng}")  
       print(f"Maths Marks: {Mat}")
       print(f"Social Marks: {Soc}")
       print(f"Science Marks: {Sci}")
       print(f"Nepali Marks: {Nep}")
       print("------------------------------")
       print(f"Your Total Marks are: {total}")
       print(f"The Percentage you have got: {per}%")
       print(f"The Grade is: {grade}")
       
       print("------------------------------")
marksheet()
        
