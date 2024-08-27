from typing import Optional, List, Dict
from difflib import get_close_matches
import random
import json

def load_knowledge_base(file_path:str) :
    with open(file_path, 'r', encoding='utf-8') as file:
        data: dict = json.load(file)
    return data

def check_keywords(sentence: str, keywords: List[str]) -> Optional[str]:
    for keyword in keywords:
        if isinstance(keyword, str) and isinstance(sentence, str):
            if keyword in sentence:
                print(f"Found keyword: '{keyword}' in the sentence.")
                return keyword
            else:
                print(f"Keyword: '{keyword}' not found in the sentence.")
    return None

def findMatch(user_question: str, knowledge: Dict[str, List[Dict[str, str]]]) -> Optional[str]:
    labels = [label for item in knowledge["faqs"] for label in item["label"]]

    # Check for keywords in the user question
    matched_keyword = check_keywords(user_question, labels)
    
    if matched_keyword:
        # Find the question that matches the keyword in the labels
        for item in knowledge["faqs"]:
            if matched_keyword in item["label"]:
                return item["question"]
    return None

def getAnswer(question: str, knowledge: Dict[str, List[Dict[str, str]]]) -> Optional[str]:
    faqs = knowledge.get("faqs", [])
    for item in faqs:
        # Handle if question is a list or a single string
        if isinstance(item["question"], list):
            if any(q.lower() == question.lower() for q in item["question"]):
                return random.choice(item["answer"]) if isinstance(item["answer"], list) else item["answer"]
        else:
            if item["question"].lower() == question.lower():
                return random.choice(item["answer"]) if isinstance(item["answer"], list) else item["answer"]
    return None

# Example knowledge base
# knowledge_base = {
#     "faqs": [
#         {
#             "label": ["ปรัชญาของภาควิชา", "ปรัชญา"],
#             "question": "ปรัชญาของภาควิชาวิศวกรรมคอมพิวเตอร์ มศว คืออะไร?",
#             "answer": "ปรัชญาคือ สร้างสรรค์ความรู้และนวัตกรรม ผลิตบัณฑิตเพื่อพัฒนาสังคมไทยอย่างยั่งยืน"
#         },
#         {
#             "label": ["นโยบายการคืนสินค้า", "คืนสินค้า"],
#             "question": "นโยบายการคืนสินค้าของบริษัทคืออะไร?",
#             "answer": "เรามีนโยบายคืนสินค้าในระยะเวลา 30 วันตามเงื่อนไขที่กำหนด"
#         }
#     ]
# }
knowledge_base: dict = load_knowledge_base('TestFolder/knowledgeBase.json')

# Example usage
def chat_bot():
    user_input: str = input("You : ")

    best_match_question = findMatch(user_input, knowledge_base)
    if best_match_question:
        print(f"Best match found: '{best_match_question}'")
        answer = getAnswer(best_match_question, knowledge_base)
        if answer:
            print(f"Answer: {answer}")
        else:
            print("No answer found.")
    else:
        print("No match found.")

chat_bot()
