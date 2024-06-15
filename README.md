# Learning about Agents - With some Dev,Sec,Ops examples

## Outline

We'll be asking agents powered by LLMs to create bash script.

- We start with a simple LLM call using langchain
- Then we show the ReAct pattern using langchain
- After that we create a Solo Agent with CrewAI a framework for Agents
- Next up the Ops crew joins the Dev crew to improve the script by bringing a tool that can check Bash syntax
- Finally we show how we can add the Sec crew into a predictable workflow using Langgraph

## Learnings

- We'll demystify that it's all about prompts
- Well show what goes over the wire to the LLM

## Pre-Reqs

- The notebooks assume you are using OpenAI
- and it needs the ENV VAR `OPENAI_API_KEY` set. (create a .env file for example when using VSCode )