import os
import re
import time
#from engine.helper import remove_words
# helper.py
from engine.utils import remove_words  # Import from the new utils.py






def extract_yt_term(command):
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern,command.re.IGNORECASE)
    return match.group(1) if match else None



def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string

input_string = "make a phone call to "
words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp',]

result = remove_words(input_string, words_to_remove)
print(result)


# key events like receive call, stop call, go back
def keyEvent(key_code):
    command =  f'adb shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap event used to tap anywhere on screen
def tapEvents(x, y):
    command =  f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command =  f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)

# To replace space in string with %s for complete message send
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')