def gmail(a,b,c,sub,mail):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    mail_content ="Now Time Is : "+str(a)+" : "+str(b)+" : "+str(c)+" and Subject = "+sub
    #The mail addresses and password
    sender_address = ''
    sender_pass = ''
    receiver_address = mail
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A mail from Class Remainder'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.outlook.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')



import datetime
from playsound import playsound
#alarm_hour = int(input("hour : "))
#alarm_min = int(input("mins : "))
#alarm_am = input("am/pm : ")
#mail=input("enter your mail id : ")
mail=input("Enter your mail :- ")
n=int(input("enter number of period u have : "))
subb=[]
print("enter subjcet-time :-")
for i in range(0,n):
      subb.append(input())
print(subb)
for i in range(0,n):
    print(subb[i])
    split=subb[i].split("-")
    print(split)
    sub=split[0]
    print(sub)
    split2=split[1].split(" ")
    alarm_am=split2[1]
    print(alarm_am)
    split3=split2[0].split(":")
    print(split3)
    alarm_hour=int(split3[0])
    print(alarm_hour)
    alarm_min=int(split3[1])
    print(alarm_min)
    if( alarm_am=="pm"):
        alarm_hour+=12


    # Import the required module for text 
    # to speech conversion
    from gtts import gTTS
    from playsound import playsound
    # This module is imported so that we can 
    # play the converted audio
    import os
      
    # The text that you want to convert to audio
    mytext = "now subject is"+sub
  
    # Language in which you want to convert
    language = 'en'
  
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome
    file1 = str("hello" + str(i) + ".mp3")
    myobj.save(file1)


    while True:
         if alarm_hour==datetime.datetime.now().hour and alarm_min==datetime.datetime.now().minute:
                print("NOW SUBJECT IS :",sub)
                gmail(alarm_hour,alarm_min,alarm_am,sub,mail)
                for i in range(0,6):
                    playsound(file1)
                break
