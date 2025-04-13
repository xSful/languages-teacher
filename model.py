from gigachat import GigaChat
import os
api_key = os.getenv("GIGACHAT_API_KEY")

def get_model_response(query):
    llm = GigaChat(credentials=api_key, verify_ssl_certs=False)
    response = llm.chat(query)
    return response.choices[0].message.content


if __name__ == "__main__":
    user_input = input("Enter your question: ")
    response = get_model_response(user_input)
    print(f"Model's response: {response}")