def vote_percentage(ch):
    yes=no=0
    for i in ch:
        if i == 'yes':
            yes += 1
        elif i == 'no':
            no += 1

    if (yes+no) == yes:
        print("Unanimous")
    elif ( yes/(yes+no) ) >= ( 2/3 ) :
        print("Clear majority")
    elif ( yes/(yes+no) ) >=  ( 1/2 ) and  ( yes/(yes+no) < ( 2/3 )):
        print("Simple majority")
    else:
        print("The motion failed")

ch=input("Input the votes (yes, no, or abstention) separated by spaces, then push enter: ").strip().split()
vote_percentage(ch)
