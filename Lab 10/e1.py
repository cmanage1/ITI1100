class Time:
    def __init__(self,hour,minu,sec):
        self.setTime(hour,minu,sec)
    def setTime(self,hour,minu,sec):
        sec_num=0
        min_num=0
        while(sec>=60):
            sec_num+=1
            sec=sec-60
        minu=minu+sec_num
        while(minu>=60):
            min_num+=1
            minu=minu-60
        hour=(hour%24)+ min_num
        if(hour>=0 and hour<=23):
            self.hour=hour
            if(minu>=0 and minu<=59):
                self.minute=minu
                if(sec>=0 and sec<=59):
                    self.second=sec
                else:
                    print("Seconds cant be -ve")
                    return
            else:
                print("Minutes cant be -ve")
                return
        else:
            print("Hour cant be -ve")
            return
        print(str(self.hour)+":"+str(self.minute)+":"+str(self.second))
    def isbefore(self,other):
        if self.hour<other.hour:
            return True
        elif self.hour==other.hour:
            if self.minute<other.minute:
                return True
            elif self.minute==other.minute:
                if self.second<=other.second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def duration(self,other):
        print(str(abs(self.hour-other.hour))+":"+str(abs(self.minute-other.minute))+":"+str(abs(self.second-other.second)))
if __name__=="__main__":
    print("Initial time =",end=" ")
    time1=Time(12,50,34)
    print("Time set to (25,10,3)=",end=" ")
    time1.setTime(25,10,63)
    print("Time 1: ",end=" ")
    t1=Time(12,4,0)
    print("Time 2: ",end=" ")
    t2=Time(10,2,1)
    print("Is Time 1 before Time 2 =",end=" ")
    print(t1.isbefore(t2))
    print("Setting Time 2 =",end=" ")
    t2.setTime(12,45,2)
    print("Is Time 1 before Time 2 =",end=" ")
    print(t1.isbefore(t2))
    print("Duration = ",end=" ")
    t1.duration(t2)
