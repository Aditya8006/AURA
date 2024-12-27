# just a simple input-output application

from langchain_ollama import OllamaLLM

MODEL_NAME = "gemma2:2b"

llm = OllamaLLM(model=MODEL_NAME)

def main_application():
    print("Type 'done' to exit")
    while True:
        question = input("you: ")
        if question.lower() == "done":
            print("AURA: Goodbye! Have a great day.")
            return
        try:
            response = llm.invoke(question)
            print(f"AURA: {response}")
        except Exception as e:
            print(f"AURA: Sorry, there was an error: {e}")

if __name__=="__main__":
    main_application()