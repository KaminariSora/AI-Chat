import tkinter
from tkinter import *
from tkinter import scrolledtext
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
from markdown import markdown

api_key = 'AIzaSyB5eH2PXMc-OkqejaWwRtJNGSa08KDdpdQ'
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return None

def chatbot_llm(input_text):
    print(f"User: {input_text}")
    try:
        # Generate content using the model
        response = model.generate_content(input_text)
        chat_response = response.text.strip()
        print(f"Chatbot Response: {chat_response}")
        
        # Convert response to markdown
        markdown_response = markdown(chat_response)
        # print(f"Markdown Response: {markdown_response}")
        
        return chat_response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Error generating response."

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

class ChatApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=0)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=0)

        self.chat_display = scrolledtext.ScrolledText(root, wrap=tkinter.WORD, state='disabled', bg="#333")
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.messageInput = tkinter.Entry(root, width=40)
        self.messageInput.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.messageInput.bind("<Return>", self.sendMessage)

        self.sendButton = Button(root, text="Send", command=self.sendMessage)
        self.sendButton.grid(row=1, column=1, padx=10, pady=10)

    def sendMessage(self, event=None):
        message = self.messageInput.get()
        if message.strip():
            self.displayMessage("You", message, '#fff')
            self.messageInput.delete(0, END)
            response = chatbot_llm(message)
            self.displayMessage("Bot", response, '#fff')
            # text_to_speech(response)
        print(message)

    def displayMessage(self, sender, message, fg_color): 
        self.chat_display.configure(state='normal')
        self.chat_display.tag_config(sender, foreground=fg_color, font=20)
        self.chat_display.insert(END, f"{sender}: {message}\n", sender)
        self.chat_display.configure(state='disabled') # disable user to change information inline
        self.chat_display.yview(END) # make the last message visible on user
        
if __name__ == "__main__":
    root = Tk()
    app = ChatApp(root)
    root.mainloop()