def getCount(inputStr):
    num_vowels = 0
    # your code here
    for i in inputStr:
        if i =='a' or i =='e' or i=='i' or i=='o' or i=='u':
            num_vowels += 1
    
    return num_vowels


    def getCount(s):
    return sum(c in 'aeiou' for c in s)

    
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")