import string

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''

    while True:
        try:
            name = input("Enter the name of file you want to open: ")
            file = open(name, "r")
            break
        except FileNotFoundError:
            print("There is no file with that name. Try again.")
    return file

def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''

    dict = {}
    line = 0

    for sentance in fp:
        line += 1
        sentance = sentance.split()
        for word in sentance:
            word = word.lower()
            if word != '-' and (len(word) >= 2):
                new_word = ''
                for i in word:
                    if i.isalpha() :
                        new_word+= i
                dict[new_word] = dict.get(new_word, [] )
                dict[new_word].append(line)
    return dict

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''

    query = query.split()
    ans = []
    result = set()
    sorted_result = []

    for key, val in D.items():
        for input in query:
            if key == input:
                ans.append(val)

    if len(ans) > 0:
        result = set ( ans[0] )
        for i in range(1, len(ans)):
            result = result & set( ans[i] )#interset sets
        for j in result:
            sorted_result.append(j)
        sorted_result.sort() #sort ascending
    return sorted_result 

##############################
# main
##############################

file=open_file()
d=read_file(file)

while True:
    query = ''

    raw_query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if raw_query != 'q' and raw_query!= 'Q':
        for i in raw_query:
            if i.isalpha() or i == ' ': #remove "'", only search words
                query+= i
        list = find_coexistance( d , query)
        if ( len(list) ) > 0:
            print("The one or more words you entered coexisted in the following lines of the file:")
            print (*list)
        else:
            print("Word '" +query+ "' not in the file")
    else:
        file.close()
        break
