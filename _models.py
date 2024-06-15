from langchain_openai import OpenAI, ChatOpenAI
from langchain_community.chat_models.ollama import ChatOllama

def get_llm(name, callbacks=[]):
    llm = OpenAI(streaming=True, temperature=0 , callbacks=callbacks)

    openai_llm = ChatOpenAI(
        model="gpt-4",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        callbacks=callbacks
        # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
        # base_url="...",
        # organization="...",
        # other params...
    )

    #if name == "ollama":
    ollama_llm = ChatOllama(
        model="llama3",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        callbacks=callbacks

        # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
        # base_url="...",
        # organization="...",
        # other params...
    )

    llm = openai_llm
    return llm