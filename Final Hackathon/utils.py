# utils.py
import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)
    return True
