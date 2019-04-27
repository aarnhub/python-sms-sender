import pickle
import os
import urllib
import urllib.parse
import urllib.request
import time
import ssl
import sys
def main():
	print("\033[H\033[J")
	mainmenu()
def mainmenu():
  if not os.path.exists('smssenderdb.pickle'):
    print("1 STEP => SETUP API SETTINGS")
  choicest1 = input("""\033[1;32m     
   (`|\/|(` (`[~|\ ||\[~|)
   _)|  |_) _)[_| \||/[_|\           
\033[1;0m                                                  
    === main menu ====
    \033[1;33m
    1. Single SMS:   
    2. Bulk SMS:     
    3. API Settings: 
    4. Exit: \033[1;0m        
    Please enter your choice [1-4]: """)
  if choicest1 == "1":
    print("\033[H\033[J")
    singlesms()
  elif choicest1 == "2":
     bulksms() 
  elif choicest1 == "3":
    print("\033[H\033[J")
    apisettings()
  elif choicest1 == "4":
     print("		Bye Bye! :)")
     pass     
  else: 
    print("\033[H\033[J")
    print("You must only select either [1-4]")
    print("Please try again")
    mainmenu()
def apisettings():
  choicest = input("""\033[1;32m  
   (`|\/|(` (`[~|\ ||\[~|)
   _)|  |_) _)[_| \||/[_|\
\033[1;0m

  === = Proovl.com API Settings ===
  \033[1;33m
    1. Update Settings:
    2. Go Back:\033[1;0m
    Please enter your choice [1-2]: """)
  if choicest == "1":
          input_number = input("  \033[1;32m1.Enter Proovl.com Phone number\033[1;0m\n")
          input_userid = input("  \033[1;32m2.Enter Proovl.com UserID\033[1;0m\n") 
          input_token = input("   \033[1;32m3.Enter Proovl.com Token\033[1;0m\n") 
          try:
              with open('smssenderdb.pickle', 'wb') as wfp:
               pickle.dump((input_number, input_userid, input_token), wfp, protocol=pickle.HIGHEST_PROTOCOL)
              print("\033[H\033[J")
              print("=== Saved! Current data: ===")
              with open('smssenderdb.pickle', 'rb') as rfp:
               otput = pickle.load(rfp)
              print("\033[1;33m=== Number: " + otput[0] + "\033[1;0m")
              print("\033[1;33m=== UserID: " + otput[1] + "\033[1;0m")
              print("\033[1;33m=== Token: " + otput[2] + "\033[1;0m")       
          except:
              print("Something wrong. Check files permissions.")
          finally:
              mainmenu()
              return   
  elif choicest == "2":
    print("\033[H\033[J")
    mainmenu()                                 
  else:
           print("\033[H\033[J")
           print("You must only select either [1-2]")
           print("Please try again")
           apisettings()

def singlesms():
  print ("""\033[1;32m 
   (`|\/|(` (`[~|\ ||\[~|)
   _)|  |_) _)[_| \||/[_|\
 \033[1;0m                         
                          
  """)
  try:
              with open('smssenderdb.pickle', 'rb') as rfp:
               otput = pickle.load(rfp)
              from2 = otput[0]
              user1 = otput[1]
              token1 = otput[2]       
  except:
    print("\033[1;33mAfter sending, please check Api settings. It can't be empty \033[1;0m")
    from2 = "44555555555"
    user1 = "Empty"
    token1 = "Empty"

  finally: 
    user = user1   # change ***** to your Proovl user ID
    token = token1  # change ***** to your Proovl token
    from_n = from2  # change ***** to your Proovl SMS number
    print("\033[1;33mSettings SID:" + from_n + " UID:" + user + " token:" + token + "\033[1;0m")
    # to = "**********"    # change ***** to receiver number
    # text = "**********"

    input_var1 = input("Enter Phone number (with country code) and press Enter:\n")
    input_var2 = input("Enter Text and press Enter:\n: ")

    print ("You entered Number: " + "\033[1;32m" + input_var1 + "\033[1;0m") 
    print ("You entered Text: " + "\033[1;32m" + input_var2 + "\033[1;0m") 


    url = "https://www.proovl.com/api/send.php?"   
    params = {       
    "user": user,       
    "token": token,       
    "from": from_n,
    "to": input_var1,
    "text": input_var2} 
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context
        query_string = urllib.parse.urlencode(params)      
        http_req = url + query_string 
        f = urllib.request.urlopen(http_req)
        txt = (f.read().decode('utf-8'))
        x = txt.split(";")
        g = x[1].replace("\"","")
        y = x[0].replace("\"","")
    if x[0] == "Error":

      print("\033[1;31m[Error message]\033[1;0m",x[1])
    else:
      print("\033[1;32m[Message has been sent!]\033[1;0m ID:",x[1])
    f.close()
    if input("Send new message? \033[1;32m(Y/N)\033[1;0m").strip().upper() != 'Y':
      print("\033[H\033[J")
      mainmenu()
      return
    else:
      print("\033[H\033[J")
      singlesms()

def bulksms():
  print("\033[H\033[J")
  print (""" \033[1;32m
   (`|\/|(` (`[~|\ ||\[~|)
   _)|  |_) _)[_| \||/[_|\
       \033[1;0m                   
                          
  """)  
  try:
              with open('smssenderdb.pickle', 'rb') as rfp:
               otput = pickle.load(rfp)
              from2 = otput[0]
              user1 = otput[1]
              token1 = otput[2]       
  except:
    print("\033[1;33mAfter sending, please check Api settings. It can't be empty \033[1;0m")
    from2 = "44555555555"
    user1 = "Empty"
    token1 = "Empty"

  finally:   
    user = user1   # change ***** to your Proovl user ID
    token = token1   # change ***** to your Proovl token
    from1 = from2  # change ***** to your Proovl SMS number
    print("\033[1;33mSettings SID:" + from1 + " UID:" + user + " token:" + token + "\033[1;0m")
    int_string = input("Enter phone numbers, separated by comma: \n")
    input_string2 = input("Enter Text and press Enter: \n")
    numbers = int_string.split(",")

    messagesSent = 0
    host = "https://www.proovl.com/api/send.php?"
    for x in numbers:
      messagesSent += 1
      params = {
      "user": user,       
      "token": token,
      "from": from1,
      "text": input_string2,
      "to": x}
      try:
        _create_unverified_https_context = ssl._create_unverified_context
      except AttributeError:
        pass
      else:
        ssl._create_default_https_context = _create_unverified_https_context
      query_string = urllib.parse.urlencode(params)   
      http_req = host + query_string
      f = urllib.request.urlopen(http_req)
      txt = (f.read().decode('utf-8'))
      z = txt.split(";")
      time.sleep(0.5)
      print("\033[1;32mProgress: {}/{}\033[1;0m".format(messagesSent, len(numbers)), (x),("" + z[1] + ""))
    if z[0] == "Error":
      print("\033[1;31m== Error. Text messages not sent ==\033[1;0m")
    else:
      print("\033[1;32m== All messages has been sent! ==\033[1;0m")
    f.close()
    if input("Send new message? \033[1;32m(Y/N)\033[1;0m").strip().upper() != 'Y':
      print("\033[H\033[J")
      mainmenu()
      return
    else:
      print("\033[H\033[J")
      bulksms()
      
main()