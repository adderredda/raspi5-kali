import requests
from bs4 import BeautifulSoup

def find_answer(question):
    url = f"https://www.google.com/search?q={question}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    answer = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')[0].get_text(separator=u' ')
    
    print(f"Answer to '{question}': {answer}")

while True:
    user_question = input("Enter your question (or type 'exit' to quit): ")
    if user_question.lower() == 'exit':
        break
    find_answer(user_question)
