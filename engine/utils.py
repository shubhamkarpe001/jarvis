# utils.py
import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Or change index for different voices
    engine.setProperty('rate', 174)  # Adjust speech rate
    engine.say(text)
    engine.runAndWait()

# utils.py
def remove_words(input_string, words_to_remove):
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string = ' '.join(filtered_words)
    return result_string
