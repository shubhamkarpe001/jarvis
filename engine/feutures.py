import os
import os
import time
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import re
from engine.helper import extract_yt_term
import pvporcupine
import subprocess
import pyautogui
from urllib.parse import quote
import time
# import cursor
import sqlite3
# from engine.feutures import findContact

from engine.utils import remove_words
from hugchat import hugchat
#import remove_words
# import quote
# import subprocess
# import pyautogui
  

# Play assistant sound function
@eel.expose
def playAssistantsound():
    music_dir = "www\\assets\\audio\\intercom-in-83962.mp3"
    playsound(music_dir)

def openCommand(query):
    speak("Opening " + query)
    
    # Clean up the query by removing the assistant's name and the word 'open'
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").strip()
    
    if query:  # If query is not empty, try to open the application
        speak(f"Opening {query}")
        
        try:
            # Use os.system to open the application (works on Windows)
            os.system(f'start {query}')  # Will work for programs like "notepad", "chrome", etc.
        except Exception as e:
            speak(f"Sorry, I couldn't open {query}.")
            print(e)
    else:
        speak("Application not found.")
        
    app_name = query.strip()    
        
    if app_name != "":
        
        try:
            cursor.execute(
                'SELECT PATH FROM sys_command WHERE name in (?)',(app_name))
            results = cursor.fetchall()
            
            if len(result) !=0:
                speak("Opening "+query)
                os.startfile(results[0][0])
            
            elif len(results) == 0:
                cursor.excute(
                    'SELECT url FROM web_command WHERE name IN (?)',(app_name))
                results = cursor.fetchall()
            
            if len(result) !=0:
                speak("Opening "+query)
                webbrowser.startfile(results[0][0])
                
            else:
                speak("Opening "+query)
                try:
                    os.system('start '+query)
                except:
                    speak("not found")
        except:
            speak("some thing went wrong")
                
                

                
                    




#eel.init('web')  # Initialize the web folder containing your HTML/JS
#eel.start('index.html')  # Start your web app (ensure this is correct path)
      
def PlayYoutube(query):
    search_term =  extract_yt_term(query)
    speak("Playing "+search_term+"on YouTube")
    kit.playonyt(search_term)


def extract_yt_term(command):
    # difine a reguler expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # use to serch a find command
    match = re.search(pattern,command,re.IGNORECASE)
    # if a match is found return the extracted song
    return match.group(1) if match else none

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        porcupine=porcupine.create(keyword=["jarvis","alexa"])
        paud=pyaudio.pyaudio()
        audio_stream=paud.open(rate=porcupine.simple_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_form("h"*porcupine.frame_length,keyword)
            
            keyword_index=porcupine.process(keyword)
            
            if keyword_index>=0:
                print("hotword detected")
                
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
            
            
    # Whatsapp Message Sending
def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)
    
    # Establish a database connection and create a cursor
    conn = sqlite3.connect('jarvis.db')  # Make sure this path is correct for your database
    cursor = conn.cursor()

    try:
        print(f"Searching for contacts: {query}")
        query = query.strip().lower()

        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ?", ('%' + query + '%',))
        results = cursor.fetchall()
        
        if results:
            print(f"Found contact: {results[0][0]}")
            mobile_number_str = str(results[0][0])
            if not mobile_number_str.startswith('+91'):
                mobile_number_str = '+91' + mobile_number_str
            return mobile_number_str, query
        else:
            speak(f"Contact '{query}' not found in the database.")
            return None, None

    except Exception as e:
        speak(f"Error: {e}")
        return None, None

            
          
def whatsApp(mobile_no, message, flag, name):
    try:
        if flag == 'message':
            target_tab = 12
            jarvis_message = f"Message sent successfully to {name}"

        elif flag == 'call':
            target_tab = 7
            message = ''
            jarvis_message = f"Calling {name}"

        else:
            target_tab = 6
            message = ''
            jarvis_message = f"Starting video call with {name}"

        # Encode the message for URL
        encoded_message = quote(message)

        # Construct the WhatsApp URL
        whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

        # Debug: Print URL to check the correct command
        print(f"WhatsApp URL: {whatsapp_url}")

        # Construct the full command to open WhatsApp
        full_command = f'start "" "{whatsapp_url}"'

        # Open WhatsApp with the constructed URL using cmd.exe
        subprocess.run(full_command, shell=True)
        time.sleep(5)
        subprocess.run(full_command, shell=True)

        # Send keystrokes to select the correct tab and send the message
        pyautogui.hotkey('ctrl', 'f')

        for i in range(1, target_tab):
            pyautogui.hotkey('tab')

        pyautogui.hotkey('enter')

        # Speak the confirmation message
        speak(jarvis_message)
        print(jarvis_message)

    except Exception as e:
        print(f"Error in WhatsApp function: {e}")
        speak('Sorry, I encountered an error while sending the message')


# chat bot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response


# android automation

def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)


# to send message
def sendMessage(message, mobileNo, name):
    from engine.helper import replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(136, 2220)
    #start chat
    tapEvents(819, 2192)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(601, 574)
    # tap on input
    tapEvents(390, 2270)
    #message
    adbInput(message)
    #send
    tapEvents(957, 1397)
    speak("message send successfully to "+name)
    