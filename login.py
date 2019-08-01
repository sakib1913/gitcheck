print"welcome to my login page"
loop='true'
while(loop=='true'):
    
     username = raw_input("username   ")
     password = raw_input("password   ")
     if(username=="sakib" and password=="abcdef"):
         print"login sucesfully   "  +   username
         loop='false'
         loop1='true'
         while(loop1=='true'):
             command=raw_input("thankyou "+username + "...")
             if(command=="exit" or command=="exit"):
                 break
             else:
                 print" "+command+"is not a valid command"
     else:
        print"invalid credintls"
        



