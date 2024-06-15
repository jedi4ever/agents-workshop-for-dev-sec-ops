from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.chat_models.ollama import ChatOllama

def get_llm(name, callbacks=[]):
    llm = OpenAI(streaming=True, temperature=0 , callbacks=callbacks)

    openai_llm = ChatOpenAI(
        model="gpt-4",
        temperature=0,
        callbacks=callbacks,
        streaming=False
    )

    #if name == "ollama":
    ollama_llm = ChatOllama(
        model="llama3",
        temperature=0,
        callbacks=callbacks,
        streaming=False
    )

    llm = ollama_llm
    llm = openai_llm
    return llm