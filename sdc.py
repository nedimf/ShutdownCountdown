import os #Importing OS module
import time #Importing Time module
import sys #Importing Sys module

#Asking user to start countdown
print "Would you like to activate shutdown countdown?"
print "Y or N"
anw = raw_input() #Getting input from the user

#Checking input form user
if anw == "Y":
    print(time.ctime())#Starting the countdown

    stime = raw_input("Select time in minutes: ")#Ask user to select time in minutes

    if stime == "++":#Set shortcut to close it in 2 hours
        print "The application will be closed at: 2 hours"
        stime = 2

    print "The application will be closed at: "+str(stime)

    seconds = int(stime)*60 #Minutes to seconds to get right value for time modul

    print (seconds)
    time.sleep(float(seconds))#Time module activated

#Checking the operation system Windows or Linux 
    if sys.platform == "win32":
         try:
             os.system("TASKKILL /IM chrome.exe /F")#Killing chrome.exe,could be any other *.exe file
         except Exception,e:
            print str(e)#Cathing exception
                    
         os.system("shutdown -s")#System shudown and letting user now that he will be logged out
   
    else:
        os.system("sudo shutdown now")#System shutdown and asking user for password

       
elif anw == "N":#Getting negative answer
    print "Ok,BYE"
    exit()#Exit the program
else:
    print "Sorry try again"#Closing program and telling user to try again
    exit()#Exit the program


