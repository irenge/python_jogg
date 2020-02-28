#students name and an ICT grade based on Homework(/25), Assessment(/50), Final Exam(/100).
def grade(score):
    if(score >= 70):
        strr = "1st"
    elif(score>=60):
        strr = "2nd"
    elif(score>=50):
        strr = "2.2"
    elif(score>=40):
        strr = "pass"
    else:
        strr = "fail"
    return strr

def calc_avg_percent(x,y,z):
    return (x + y + z)*100/175

student = list()
home = list()
assess= list()
exam =list()

num = int(input("Enter number of students :"))
for i in range(0,num):
    student.append(input("Enter student "+ str(i) +"  name: "))
    home.append(input("Enter homework /25 "+ student[i]+": "))
    assess.append(input("Enter assessment /50 "+ student[i]+": "))
    exam.append(input("Enter exam /100 "+ student[i]+": "))
    print("   =======     =======     =====   ====== ")
print(" ###################################################Display ####################################################")
for i in range(num):
    print(student[i]+" homework "+ home[i] + " Assessment " + assess[i] + " Exam " + exam[i] + " grade :"+ grade(calc_avg_percent(float(home[i]),float(assess[i]),float(exam[i]))))
