import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
from markdown import markdown

# Set up your Google API key
api_key = 'AIzaSyB5eH2PXMc-OkqejaWwRtJNGSa08KDdpdQ'
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function 1: Speech to Text
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

# Function 2: Chatbot LLM using Google Generative AI
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
        
        return markdown_response
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Error generating response."

# Function 3: Text to Speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main function to integrate all steps
def main():
    i=0
    while True:
        # input_text = speech_to_text()
        # if input_text:
        #     response = chatbot_llm(input_text)
        #     text_to_speech(response)
        input_text = ["Hello", "How are you?", "How many days in 1 week?"]
        for i in range(3):
            response = chatbot_llm(input_text[i])
            text_to_speech(response)

if __name__ == "__main__":
    main()
