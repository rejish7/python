#wap to enter marks  per and grade of student

num = int(input("Enter number of students: "))
x =1 
total_marks=[]
while x<=num:
    print(f"=========students: {x}========")
    for a in range(1):
        Nep = int(input ("Enter Nepali Marks"))
        Eng = int(input ("Enter English Marks")) 
        Maths = int(input ("Enter Maths Marks"))
        Science = int(input ("Enter Science Marks"))
        Social = int(input ("Enter Social Marks"))
        total = Nep+Eng+Maths+Science+Social
        total_marks.append(total)

    x+=1

    for total in total_marks:
        per =total/5
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
        print(f"Total Marks:{total} Percentage:{per} Grade:{grade}")