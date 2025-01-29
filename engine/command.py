
import os
import time
import pyttsx3
import speech_recognition as sr
import eel
eel.init('web')
import time

from engine.utils import speak  

# Speak function to convert text to speech
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set to second voice (you can change the index if needed)
    engine.setProperty('rate', 174)  # Set speech rate
    eel.DisplayMessage(text)
    print(text)  # Optionally print what is being spoken
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()
    
# Function to take command from microphone
def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening...')  # Corrected print statement
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1  # Adjust this to fine-tune listening sensitivity
        r.adjust_for_ambient_noise(source)  # Adjusts for background noise
        
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)  # Adjusted for better performance
            
            print('Recognizing...')
            eel.DisplayMessage('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            eel.DisplayMessage(query)
            speak(query)
            time.sleep(2)
            
            
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""  # Return empty string if speech is not understood
        
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return ""  # Return empty string if there's an issue with the API request
        
    return query.lower()


@eel.expose
def allCommands(message=1):
    
    
    if message == 1:
        query = takecommand()
        print(f"Received command: {query}")
        eel.senderText(query)
    
    else:
        query = message
        eel.senderText(query)
        
    try:
        
        

        from engine.feutures import findContact, whatsApp, makeCall,sendMessage
        contact_no, name = findContact(query)
        
        if(contact_no != 0):
                
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
        # Handle open command
        elif "open" in query:
            from engine.feutures import openCommand
            openCommand(query)

        # Handle youtube play command
        elif "on youtube" in query:
            from engine.feutures import PlayYoutube
            PlayYoutube(query)

        else:
            # print("Command not recognized")
            # speak("Command not recognized. Please try again.")
            print("Command passed to chatbot:", query)
            from engine.feutures import chatBot
            chatBot(query)

    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred. Please try again.")

    eel.ShowHood()
    




