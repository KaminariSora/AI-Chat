import json
import random
import pyttsx3
from difflib import get_close_matches
from typing import List, Optional, Dict

def load_knowledge_base(file_path:str) :
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path:str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2) 

def find_best_match(user_question:str, question:list[str]) -> Optional[str]:
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: Dict[str, List[Dict[str, str]]]) -> Optional[str]:
    for item in knowledge_base["question"]:
        if isinstance(item["question"], list):
            for q in item["question"]:
                if q.lower() == question.lower():
                    return random.choice(item["answer"]) if isinstance(item["answer"], list) else item["answer"]
        else:
            if item["question"].lower() == question.lower():
                return random.choice(item["answer"]) if isinstance(item["answer"], list) else item["answer"]
    return None
        
def text_to_speech(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
        
def chat_bot():
    knowledge_base: dict = load_knowledge_base('TestFolder/knowledgeBase.json')

    while True:
        user_input: str = input("You : ")
        if user_input.lower() == ["quit", "exit"]:
            break

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["question"]])
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot : {answer}")
            text_to_speech(answer)
        else:
            notice = "I don't know the answer. Can you teach me?"
            print(f"Bot : {notice}")
            text_to_speech(notice)
            new_answer = str = input("type the answer or 'skip' to skip : ")

            if new_answer.lower() != 'skip':
                knowledge_base["question"].append({"question" : user_input, "answer": new_answer})
                save_knowledge_base('knowledgeBase.json', knowledge_base)
                thx = "Thank you for teaching me!"
                print(f"Bot : {thx}")
                text_to_speech(thx)

if __name__ == '__main__':
    chat_bot()