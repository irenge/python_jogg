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

def overall(x,y,z):
    if(x>=50 and y >=50 and z >= 50):
        return "PASS"
    else:
        return "FAIL"
print("############  INPUT #####################")
bio = float(input("Enter Biology mark: "))
chem = float(input("Enter your Chemistry: "))
phys = float(input("Enter your physics: "))
print("############  CALCULATION #####################")
avg = (bio + chem + phys)/3
print("##############   OUTPUT  ######################")
print("Biology ",bio, ":",grade(bio))
print("Chemistry ",chem, ":",grade(chem))
print("Physics ",phys, ":",grade(phys))
print("===============================================")
print("average ",avg, ":",grade(avg))
print(" Status ", overall(bio,chem,phys))