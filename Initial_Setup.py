import csv

def Initial_Setup():

    print()
    print('Hello! This is LifeApp.py - your interactive personal stats monitor.')
    print('You can think of me as your personal assistant as we set this program up for you.')
    print()
    print('Speaking of which, what do you want to call me?')
    
    print('###########################################################')
    while True:
        assist_name = input()
        for letter in assist_name:
            pin_point = False
            if letter.isdigit() == True:
                print('Please enter my name as sequence of letters.')
                pin_point = True
                break
            else:
                pass
        if pin_point == False:
            break
    print('###########################################################')    
    
    print('\nGreat, my name is ',assist_name,'.', sep="")
    print()
    print('And what is your name?')
    
    print('###########################################################')
    admin_first = input('First name: ')
    admin_last = input('Last name: ')
    print('###########################################################')
    
    print('\nGreat, nice to meet you, ',admin_first," ",admin_last,'.',sep="")
    
    f = open('admin_data.csv','w')
    header = ['First name','Last name','Assistant']
    names = [admin_first,admin_last,assist_name]
    setup_complete = ["Setup complete",'','']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(names)
    writer.writerow(['','',''])
    writer.writerow(setup_complete)
    f.close
    
    print('All your personal information will be stored locally in the form of .CSV files.')
    
    #input('------------------------Press ENTER to exit.------------------------')