import os
import sys
from gtts import gTTS  # pip install gTTS
import requests
import speech_recognition as sr  # pip install speechRecognition
import datetime
import time
import cv2  # pip install opencv-python
import random
from requests import get
import wikipedia  # pip install wikipedia
import webbrowser  # pip install webbrowser
import smtplib  # pip install smtlib
import pyjokes  # pip install pyjokes
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import PyPDF2  # pip install PyPDF2
from PyQt5 import QtGui  # pip install PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from FridayUI import Ui_friday  # from the UI program
import audioplayer  # pip install audioplayer
import wolframalpha  # pip install wolframalpha


class person:  # user name setting
    name = ""

    def setName(self, name):
        self.name = name


class friday:  # assistant name setting
    name = ""

    def setName(self, name):
        self.name = name


person_obj = person()
friday_obj = friday()
friday.name = ""
person_obj.name = ""


def speak(audio):  # to speak
    tts = gTTS(audio)
    tts.save("friday.mp3")
    audioplayer.AudioPlayer("friday.mp3").play(block=True)


def wish():  # to wish
    hour = int(datetime.datetime.now().hour)

    if hour >= 8 and hour < 12:
        speak("good morning")
    elif hour >= 13 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am friday sir. please tell me how can i help you")


def news():  # to news api
    # paste your key in the dash
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=___________________"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = [
        "fist",
        "second",
        "third",
        "fourth",
        "five",
        "six",
        "seven",
        "eight",
        "ninth",
        "tenth",
    ]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


def tellDay():  # to tell day

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }

    if day in Day_dict:
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def date():  # to tell date
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)


def screenshot():  # to take screenshot
    img = pyautogui.screenshot()
    img.save("screen.png")


def cpu():  # to cpu ststs
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()

    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    speak("battery is at ")
    speak(percent + "% | " + plugged)


def cam():  # to camera
    video_capture = cv2.VideoCapture(0)

    cv2.namedWindow("Facecam")

    while True:
        ret, frame = video_capture.read()
        cv2.imshow("Facecam", frame)

        # This breaks on 'q' key
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def pdf_reader():  # to read pdf
    book = open(input("enter path to pdf:"), "rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.getNumPages()
    speak(f"total number of pages in this book {pages}")
    speak("please enter a page number from 0 to something i have to read")
    pg = int(input("enter here:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def support():  # to contact suport
    url = "https://github.com/https-github-com-zameel28/F.R.I.D.A.Y"
    webbrowser.get().open(url)


def setup():  # setup audio
    list1 = ["Ironman Airborne.mp3", "Iron Man Music.mp3", "Iron Man.mp3"]
    audioplayer.AudioPlayer(random.choice(list1)).play(block=True)


def intro():  # intro audio
    list2 = ["Ironman Airborne.mp3", "Iron Man Music.mp3", "Iron Man.mp3"]
    audioplayer.AudioPlayer(random.choice(list2)).play(block=True)


class MainThread(QThread):  # main
    def run(self):
        self.TaskExecution()

    @staticmethod
    def takecommand():  # speech-to-text
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

    def TaskExecution(self):  # main task execution
        setup()
        wish()
        while True:
            self.query = self.takecommand().lower()

            if "open calender" in self.query:
                url = "https://calendar.google.com/calendar/u/0/r?tab=rc"
                webbrowser.get().open(url)

            elif "open command prompt" in self.query:
                os.system("start cmd")   #to open cmd 

            elif "open camera" in self.query:
                cam()

            elif "ip address" in self.query:
                ip = get("http://api.ipify.org").text
                speak(f"your ip address is {ip}")

            elif "introduce yourself" in self.query:
                intro()
                speak("I am created by zameel ali, subhash and naveen")
                speak("I was made by using python")
                speak("i am born on 11th oct 2021")
                speak("hope you got the information")

            elif "time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Sir, the time is {strTime}")

            elif "take a screenshot" in self.query:
                screenshot()
                speak("Done!")

            elif "support" in self.query:
                support()

            elif "stock price of" in self.query:
                search_term = self.query.split("for")[-1]
                url = "https://google.com/search?q=" + search_term
                webbrowser.get().open(url)
                speak("Here is what I found for " + search_term + " on google")

            elif "open youtube" in self.query:
                search_term = self.query.split("for")[-1]
                search_term = search_term.replace("open youtube", "").replace(
                    "search", ""
                )
                url = "https://www.youtube.com/results?search_query=" + search_term
                webbrowser.get().open(url)
                speak("Here is what I found for " + search_term + "on youtube")

            elif "wikipedia" in self.query:
                speak("serching wikipedia")
                self.query = self.query.replace("wikipedia")
                result = wikipedia.summary(self.query, sentence=2)
                speak("according to wikipedia:")
                speak(result)
                print(result)

            elif "search google" in self.query:
                speak("sir, what should i search")
                cm = self.takecommand().lower()
                webbrowser.get.open(f"{cm}")

            elif "how are you" in self.query:
                list3 = ["I'm fine, glad you me that", ""]
                speak(random.choice(list3))

            elif "i love you" in self.query:
                speak("It's hard to understand")

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = self.takecommand()
                file = open("friday.txt", "w")
                speak("Sir, Should i include date and time")
                snfm = self.takecommand().lower()
                if "yes" in snfm or "sure" in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "day" in self.query:
                tellDay()

            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("friday.txt", "r")
                print(file.read())
                speak(file.read())

            elif "route to" in self.query:
                search_term = self.query.split("to")[-1]
                url = "https://www.google.co.in/maps/dir/" + search_term
                webbrowser.get().open(url)
                speak("Here is what I found for" + search_term + "on google maps")

            # add more url's

            elif "ask" in self.query or "question" in self.query:
                speak(
                    "I can answer to computational and geographical questions  and what question do you want to ask now"
                )
                question = self.takecommand().lower()
                app_id = "your key"
                client = wolframalpha.Client(app_id)
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif "send email" in self.query:
                speak("What should i say")
                self.query = self.takecommand().lower()

                email = input("Enter your email ID: ")
                password = input("Enter password: ")
                send_to_person = input("Enter the reciver ID:")
                message = self.query

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_person, message)
                server.quit()
                speak("email has been sent to %s" % send_to_person)

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get("https://api.ipify.org").text
                    print(ipAdd)
                    url = "https://get.geojs.io/v1/ip/geo" + ipAdd + ".json"
                    geo_request = requests.get(url)
                    geo_data = geo_request.json()
                    city = geo_data["city"]
                    country = geo_data["country"]
                    speak(
                        f"sir i an not sure, but i think we are in {city} city of {country} country"
                    )
                except Exception as e:
                    print(e)
                    speak("sorry sir")

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "change window" in self.query:
                speak("switching windows")
                pyautogui.keyDown("alt")
                pyautogui.keyDown("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait sir, fetching the latest news")
                news()

            elif "read pdf" in self.query:
                pdf_reader()

            elif "sleep now" in self.query:
                speak("okay sir")
                break

            elif "activate how to do mode" in self.query:
                from pywikihow import search_wikihow

                speak("activated how to do mode")
                how = self.takecommand()
                max_result = 1
                how_to = search_wikihow(how, max_result)
                if len(how_to) != 1:
                    raise AssertionError
                how_to[0].print()
                speak(how_to[0].summary)

            elif "exit" in self.query:
                sys.exit()

            elif (
                "hey" in self.query
                or "hi" in self.query
                or "hello" in self.query
                or "ok" in self.query
            ):
                greetings = [
                    "hey, how can I help you" + person_obj.name,
                    "hey, what's up?" + person_obj.name,
                    "I'm listening" + person_obj.name,
                    "how can I help you?" + person_obj.name,
                    "hello" + person_obj.name,
                ]
                greet = greetings[random.randint(0, len(greetings) - 1)]
                speak(greet)

            elif (
                "what is your name" in self.query
                or "what's your name" in self.query
                or "tell me your name" in self.query
            ):

                if person_obj.name:
                    # gets users name from voice input
                    speak(f"My name is {friday.name}, {person_obj.name}")
                else:
                    # incase you haven't provided your name.
                    speak(f"My name is {friday_obj.name}. what's your name sir?")

            elif "my name is" in self.query:
                person_name = self.query.split("is")[-1].strip()
                speak("okay, i will remember that sir" + person_name)
                # remember name in person object
                person_obj.setName(person_name)

            elif "what is my name" in self.query:
                speak("Your name must be " + person_obj.name)

            elif "your name should be" in self.query:
                friday_name = self.query.split("be")[-1].strip()
                speak("okay, i will remember that my name is " + friday_name)
                friday.setName(friday_name)  # remember name in asis object

            elif "how are you" in self.query or "how are you doing" in self.query:
                speak("I'm very well, thanks for asking " + person_obj.name + "sir")

            elif "toss coin" in self.query or "flip coin" in self.query:
                moves = ["head", "tails"]
                cmove = random.choice(moves)
                speak("I chose " + cmove)


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_friday()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("untitled-6.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


# the UI


app = QApplication(sys.argv)
friday = Main()
friday.show()
sys.exit(app.exec_())
