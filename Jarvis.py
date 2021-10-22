import pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import smtplib 
from secrets import senderemail, epwd, to
from email.message import EmailMessage
#import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def getvoices(voice):
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        speak("hello, this is jarvis. at your Service, sir!")

    if voice == 2:
        engine.setProperty('voice', voices[1].id)
        speak("hello, this is Friday.")

#time func
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(" the current time is: ")
    speak(Time)
    

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is: ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Sir")
    elif hour >= 12 and hour < 18: 
        speak("Good Afternoon Sir")
    elif hour >=18 and hour < 24:
        speak("Good Evening Sir")
    else:
        speak("Happy to serve you Mr. John. But, dont you think. its kinda late?")

def wishme():
    speak("Welcome back Mr. John")
    #time()
    #date()
    greeting()
    speak("Im at your service, please tell me how may i serve you")
# while True:
#     voice = int(input("Press 1 for male \nPress 2 for female \n "))
#     speak(audio)
#     getvoices(voice)

#getvoices()

#wishme()

def takeCommandCMD():
    query = input("Please tell me how may i serve you?  \n")
    return query

def takeCommandMic(): #mic opener
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening ...")
        r.energy_threshold = 4000
        r.pause_threshold = 1
        audio = r.listen(source)
        #stocking the audio in the audio variable

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-US ")
        print(query)
    except Exception as e:
        print(e)
        speak("Can you repeat that sir?")
        return "None"
    return query

def sendEmail(reciever, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
     #tls means transport layer security
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


if __name__ == "__main__":
    getvoices(2)
    wishme()
    while True:
        query = takeCommandMic().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        
        elif 'dumb' in query:
            speak("well; you; created me. sooooo.")
        
        elif 'email' in query:
            email_list = {
                '1': 'jk_falcasantos@yahoo.com',
                'primary 2': 'rykendo999@gmail.com',
                'primary 3' : 'nezhat.kaddour@gmail.com',
                'primary 4': 'melissa.hua29@gmail.com',
                'primary five': 'henry.le2k1@gmail.com'
                
            }
            try:
                speak("to whom you want to send the mail?")
                name = takeCommandMic()
                receiver = email_list[name]
                speak('what is the subject of your mail sir?')
                subject = takeCommandMic()
                speak('what should i say sir?')
                content = takeCommandMic()
                sendEmail( receiver , subject,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("unable to end the mail")
        
        elif 'wikipedia' in query:
            speak('very well sir. ')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences= 2)
            print(result)
            speak(result)


        elif 'offline' in query:
            speak('very well sir. and fuck you!')
            quit()
            
            # if 'yes' in query:
            #     speak('very well sir, shutting down')
            #     quit()
            # elif 'sorry' in query:
            #     speak('i knew it!, you bitch!')


