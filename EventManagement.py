from queue import Queue
from ticket import ticket
import os
class Admin:
    __USERName=None
    __Password=None
    __Queue=None
    __eventsQ=None
    def __init__(self)->None :
      self.__USERName="admin"
      self.__Password="admin123123"
      self.__Queue=Queue()
      self.splitEvents(self.importUsers('Text.txt'))
    def getName(self):
       return self.__USERName
    def getPassword(self):
       return self.__Password
    def getUserName(self):
       return self.__USERName
    def getPassword(self):
       return self.__Password
    def getUsers(self):
       return self.__Queue
    def importUsers(self,file):
      try:
        with open(file) as file:
          data=file.read()
          dataspl=data.splitlines()
          file.close()
      except FileNotFoundError:
        print('File not found')
      return dataspl
    def sortFiles(self):
       try:
          with open('path') as file:
             ls=file.read().split(',')
             for x in ls:
                if not x=='':
                    q=Queue()
                    try:
                        with open(x) as file:
                            ls_2=file.read().splitlines()
                            for y in ls_2:
                              if y !='':
                                q.enQueue(ticket(*y.split(',')))
                            file.close()
                    except FileNotFoundError:
                        print('File not found')
                    q.Sorting()
                    st=''
                    for _ in range(q.size()):
                     st+=f'{q.deQueue().toString()}\n'
                    try:
                        with open(x,'w') as file:
                            ls_2=file.write(st)
                            file.close()
                    except FileNotFoundError:
                        print('File not found')
       except FileNotFoundError:
            print('File not found')
          
    def splitEvents(self,dataspl):
       events={}
       path=''
       for x in dataspl:
            if not x=='':
                lis=x.split(',')
                self.__Queue.enQueue(ticket(lis[0],lis[1],lis[2],lis[3],int(lis[4])))
                if lis[1] in list(events.keys()):
                    events[lis[1]].append(ticket(lis[0],lis[1],lis[2],lis[3],int(lis[4])).toString())
                else:
                    events.update({lis[1]:[ticket(lis[0],lis[1],lis[2],lis[3],int(lis[4])).toString()]})
       self.__eventsQ=events
       for key,value in events.items():
          try:
            with open(f"{key}.txt",'w') as file:
                _str=""
                for x in value:
                   _str+=f'{x}\n'
                file.write(_str)
                file.close()
          except FileNotFoundError:
             print('File not found')
       self.sortFiles()
        
       for x in list(events.keys()):
          path+=f'{x}.txt,'
       path+='Text.txt'
       try :
            with open('path.txt','w') as file:
                file.write(path)
                file.close()
       except FileNotFoundError:
           print('File not found')
    def displayStatics(self):
       self.splitEvents(self.importUsers('Text.txt'))
       print(f'the total of the tickets :{self.__Queue.size()}')
       for key,value in self.__eventsQ.items():
          print(f"the static of {key} event is:{len(value)} tickets")
    
    def UpdateFile(self,_str):
       try:
          with open('Text.txt','w') as file:
             file.write(_str)
             file.close()
       except FileNotFoundError:
          print('File not found')
    def SaveChanges(self,q):
       _str=''
       try:
          with open('Text.txt') as file:
             _str+=file.read()
             file.close()
       except FileNotFoundError:
          print('File not found')
       _str+=f"{q.toString()}\n"
       self.UpdateFile(_str)
    
    def BooKing(self,event_Id,User_Name,Time_Stamp,priorety):
       ticket_id=int(self.__Queue.peekLast().getTikId()[4:])
       ntk=ticket_id+1
       return ticket(f"tick{ntk}",event_Id,User_Name,Time_Stamp,priorety)
    def displayAllTickets(self):
       try:
          with open('Text.txt') as file:
             print(file.read())
             file.close()
       except:
          print('File not found')
    def disableTicket(self,id):
       try:
          with open('Text.txt') as file:
            tikets=file.read().splitlines()
            s=''
            for x in tikets:
               if not x[:x.find(',')]==id:
                  s+=f"{x}\n"
            try:
               with open('Text.txt','w') as file:
                  file.write(s)
            except FileNotFoundError:
               print('File not found')
       except:
          print('File not found')
       self.splitEvents(self.importUsers('Text.txt'))
    def ticketPriorety(self,_ticket):
       lis=[]
       sort_key=lambda item :item.getPriority()
       filter_key=lambda item :item.getTikId()==_ticket
       ticketsdata=self.importUsers('Text.txt')
       for x in ticketsdata:
          lis.append(ticket(*x.split(',')))
       lis.sort(key=sort_key)
       tk=list(filter(filter_key,lis))
       i=tk[0]
       tk[0].setPriority(input('Change priority:'))
       print(f"tk={tk[0].toString()}",f"i={i.toString()}")
       lis[lis.index(i)]=tk[0]
       try:
          with open('Text.txt','w') as file:
             s=''
             for x in lis:
                s+=f'{x.toString()}\n'
             file.write(s)
             file.close()
       except FileNotFoundError:
          print('File not found')
       self.splitEvents(self.importUsers('Text.txt'))
    def RunEvent(self,ev):
       ids=[]
       try:
          with open(f'{ev}.txt') as file:
             f=file.read()
             for x in f.splitlines():
                print(x)
                ids.append(x[:x.find(',')])
       except FileNotFoundError:
          print('File not found')
       for x in ids:
          self.disableTicket(x)
       try:
         os.remove(f'{ev}.txt')
       except FileNotFoundError:
          print('File not found')
       
Admin=Admin()
Admin.splitEvents(Admin.importUsers('Text.txt'))
Admin.SaveChanges(Admin.BooKing('ev003','Afrodit','900BC0905','6'))
#Admin.disableTicket('tick003')
#Admin.RunEvent('ev102')
Admin.displayAllTickets()
Admin.displayStatics()
Admin.ticketPriorety('tick103')




