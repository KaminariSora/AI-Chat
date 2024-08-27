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


def check_keywords(sentence: str, keywords: List[str]) -> Optional[str]:
    for keyword in keywords:
        if isinstance(keyword, str) and isinstance(sentence, str):
            if keyword in sentence:
                print(f"Found keyword: '{keyword}' in the sentence.")
                return keyword
            else:
                print(f"Keyword: '{keyword}' not found in the sentence.")
    return None

def find_best_match(user_question: str, knowledge: Dict[str, List[Dict[str, str]]]) -> Optional[str]:
    labels = [label for item in knowledge["question"] for label in item["label"]]

    matched_keyword = check_keywords(user_question, labels)
    
    if matched_keyword:
        # Find the question that matches the keyword in the labels
        for item in knowledge["question"]:
            if matched_keyword in item["label"]:
                return item["question"]
    return None

def get_answer_for_question(question: str, knowledge_base: Dict[str, List[Dict[str, str]]]) -> Optional[str]:
    faqs = knowledge_base.get("question", [])
    for item in faqs:
        if isinstance(item["question"], list):
            if faqs == (question for q in item["question"]):
                return random.choice(item["answer"]) if isinstance(item["answer"], list) else item["answer"]
        else:
            if item["question"] == question:
                return random.choice(item["answer"]) if isinstance(item["answer"], list) else item["answer"]
    return None
        
def text_to_speech(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
        
def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledgeBase.json')

    while True:
        user_input: str = input("You : ")
        if user_input.lower() == ["quit", "exit"]:
            break

        best_match = find_best_match(user_input, knowledge_base)
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot : {answer}")
            # text_to_speech(answer)
        # else:
        #     notice = "I don't know the answer. Can you teach me?"
        #     print(f"Bot : {notice}")
        #     text_to_speech(notice)
        #     new_answer = str = input("type the answer or 'skip' to skip : ")

        #     if new_answer.lower() != 'skip':
        #         knowledge_base["question"].append({"question" : user_input, "answer": new_answer})
        #         save_knowledge_base('knowledgeBase.json', knowledge_base)
        #         thx = "Thank you for teaching me!"
        #         print(f"Bot : {thx}")
        #         text_to_speech(thx)

if __name__ == '__main__':
    chat_bot()