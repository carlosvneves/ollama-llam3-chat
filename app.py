from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """

Responda a seguinte pergunta:


Aqui está o contexto: 
{context}


Aqui está a questão:
{question}

Resposta:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

def handle_chat():
    context = ""
    while True:
        question = input("Sua pergunta (ou digite 'q' para sair): ")
        if question.lower() == "q":
            break
        result = chain.invoke({"context":context,"question":question})
        print(f"Bot: \n{result}\n")
        context += f"\nUser:{question}\nAI:{result}\n" 

if __name__ == "__main__":
    print("Bem-vindo ao Chatbot!")
    handle_chat()
