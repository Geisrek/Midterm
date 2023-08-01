from EventManagement import Admin
Main=None
def AdminPlatform():
    admin=Admin('Text.txt')
    option=input('1. Display Statistics\n2. Book a Ticket\n3. Display all Tickets\n4. Change Ticket’s Priority\n5. Disable Ticket\n6. Run Events\n7. Exit\nYour Option:')
    if option == '1':
        admin.displayStatics()
        AdminPlatform()
    elif option =='2':  
        event_Id=input('Enter the event Id:')
        User_Name=input('Enter the User Name:')
        Time_Stamp=input('Enter the date yyymmdd:')
        priorety=input('Enter the prioritie:')
        admin.SaveChanges(admin.BooKing(event_Id,User_Name,Time_Stamp,priorety))
        admin.splitEvents(admin.importUsers('Text.txt'))
        AdminPlatform()
    elif option=='3':
        admin.displayAllTickets()
        AdminPlatform()
    elif option=='4':
        admin.ticketPriorety(input('Enter the ticket id: '))
        AdminPlatform()
    elif option=='5':
        admin.disableTicket(input('Enter the ticket id:'))
        AdminPlatform()
    elif option=='6':
        try:
            with open('path') as file:
                admin.RunEvent(input(f'input rhe event from the following {file.read()[:file.read().find("T")]}:'))
        except FileNotFoundError:
            print('File Not Found')
        AdminPlatform()
    elif option==7:
      Main()
        

def NormalUserPlatform(User_Name,main=None):
    option=input('1.Book a ticket\n2.Exit\nYour option:')
    admin=Admin('Text.txt')
    if option=='1':
       try:
          with open('path') as file:
            evs=file.read().split(',')
            event_Id=input(f'Enter the event Id \n{evs} please choose one of them :')
            if not f'{event_Id}.txt' in evs:
              print('wrong event')
              NormalUserPlatform(User_Name)
            else:
              Time_Stamp=input('Enter the date yyymmdd:')
              admin.SaveChanges(admin.BooKing(event_Id,User_Name,Time_Stamp,'0'))
              admin.splitEvents(admin.importUsers('Text.txt'))
              NormalUserPlatform(User_Name)
       except:
          print('Error!')
       
    elif option=='2':
        main()
    else:
        print('wrong choise')
        NormalUserPlatform(User_Name,main)
def main():
    Run=input('If you want to terminate the program press 0 \nif you want to continue press any key\n your option:')
    if Run=='0':
         print('program is turminated')
    else:
        User_name=input('Enter User Name:')
        Password=input('Enter Password:')
        admin=Admin('Text.txt')
        if User_name==admin.getName() and Password==admin.getPassword():
            AdminPlatform()
        elif Password=='' and not User_name=='':
            NormalUserPlatform(User_name,main)
        elif User_name=='':
            print(f'Invalid User Name [{User_name}]\n please try again')
            main()
        else:
            print('Incorrect Usernameand/or Password')
            main()
Main=main()
main()