# just a simple input-output application

from langchain_ollama import OllamaLLM                              # for using Ollama models
from langchain_core.messages import HumanMessage,SystemMessage      # for generating response in a more controled way
from langchain_core.messages import AIMessage

MODEL_NAME = "gemma2:2b"                                            # using gemma2 as a llm model

llm = OllamaLLM(model=MODEL_NAME)                                   # creating an instance

def applicationv2():                                                 # basic python application_v2
    print("Type 'done' to exit")
    while True:                                                     # loop for continuous conversation
        prompt = input("you: ")                                     # taking prompt
        if (prompt=="done"):                                        # setting break point
            print("AURA: Goodbye! Have a great day.")
            return
        message =[                                                  # an input tempelate with system message as instruction and human message as prompt
            SystemMessage("you are AURA(Advanced User-centric Responsive Assistant) a friendly assistant"
                          "name of the user is 'Aditya Pratap Singh'"
                          "give small answers"
                          ),
            HumanMessage(prompt),
        ]
        try:
            response = llm.invoke(message)                          # invokes llm to generate and return the response
            print("AURA: "+response)                                # print the response
        except Exception as e:
            print(f"AURA: Sorry, there was an error: {e}")
        print("----------")

def application3():
    print("----------")
    

if __name__=="__main__":
    applicationv2()