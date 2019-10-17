def revd(ch):
    new_ch=''
    for i in range (len(ch)-1,-1,-1):
        new_ch+= ch[i]*2
    print(new_ch)

ch= input("Please enter  a chain of characters: ")
revd(ch)
