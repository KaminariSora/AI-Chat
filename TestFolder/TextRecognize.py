import nltk
from nltk.corpus import words

# Download the words corpus if not already done
nltk.download('words')

# Get a set of English words
word_list = set(words.words())

def segment_text(text):
    segmented_text = ""
    while text:
        for i in range(len(text), 0, -1):
            word_candidate = text[:i]
            if word_candidate in word_list:
                segmented_text += word_candidate + " "
                text = text[i:]
                break
        else:
            segmented_text += text[0] + " "
            text = text[1:]
    return segmented_text.strip()

def chatbot():
    print("bot: please write anything.")
    
    while True:
        user_input = input("Input: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        
        segmented_text = segment_text(user_input)
        print(f"bot: I think you said: {segmented_text}")

if __name__ == "__main__":
    chatbot()
