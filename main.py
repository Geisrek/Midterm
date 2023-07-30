from EventManagement import Admin
Main=None
def AdminPlatform():
    admin=Admin()
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
        

def NormalUserPlatform(User_Name,main):
    option=input('1.Book a ticket\n2.Exit\nYour option:')
    admin=Admin()
    if option=='1':
       event_Id=input('Enter the event Id:')
       Time_Stamp=input('Enter the date yyymmdd:')
       admin.SaveChanges(admin.BooKing(event_Id,User_Name,Time_Stamp,'0'))
       admin.splitEvents(admin.importUsers('Text.txt'))
       NormalUserPlatform(User_Name)
    elif option=='2':
        main()
    else:
        print('wrong choise')
        NormalUserPlatform(User_Name)
def main():
    Run=input('If you want to terminate the program press 0 \nif you want to continue press any key\n your option:')
    admin=Admin()
    if Run=='0':
         print('program is turminated')
    else:
        User_name=input('Enter User Name:')
        Password=input('Enter Password:')
        if User_name==admin.getName() and Password==admin.getPassword():
            AdminPlatform()
        elif Password=='' and not User_name=='':
            NormalUserPlatform(User_name,main)
        elif User_name=='':
            print(f'Invalid User Name [{User_name}]\n please try again')
            main()
        else:
            print('wrong User Name or Password please try again')
            main()
Main=main()
main()