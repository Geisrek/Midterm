import datetime#https://www.geeksforgeeks.org/get-current-timestamp-using-python/
class USER:
    __Tik_id=None
    __Tik_ev=None
    __User_Name=None
    __Time_stamp=None
    __priority=None
    def __init__(self,id,ev,User,time,prio) -> None:
        self.__Tik_id=id
        self.__Tik_ev=ev
        self.__User_Name=User
        self.__Time_stamp=time
        self.__priority=prio
    def getTikId(self):
        return self.__Tik_id
    def getTikEv(self):
        return self.__Tik_ev
    def getUserName(self):
        return self.__User_Name
    def getTime(self):
        return self.__Time_stamp
    def getPriority(self):
        return self.__priority
    def setPriority(self,item):
        self.__priority=item
    def toString(self):
        return f"{self.__Tik_id},{self.__Tik_ev},{self.__User_Name},{self.__Time_stamp},{self.__priority}"