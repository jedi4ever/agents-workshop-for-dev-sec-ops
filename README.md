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

- The notebooks assume you are using OpenAI
- and it needs the ENV VAR `OPENAI_API_KEY` set. (create a .env file for example when using VSCode )

## GitHub CodeSpaces

To keep things as simple as possible you can run this workshop in GitHub CodeSpaces.  Simply hit the `Launch Lab` link below and a new codespace will open. The CodeSpace will be an embedded VSCode with Jupyter Notebook pre-configured and ready to go.

> Note: It may take a few moments for Python to be ready.  Once the Lab is ready open the `0_welcome.ipynb` file to begin the lab.
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/jedi4ever/agents-workshop-for-dev-sec-ops)

Once you have finished the workshop you should [Manage](https://github.com/jedi4ever/agents-workshop-for-dev-sec-ops/codespaces) your codespaces and delete the codespace instance.