from crewai import Agent

def get_agent_by_name(name, llm):
    if name == 'senior developer':
        print("Creating senior developer")
        return senior_developer(llm)
    elif name == 'senior devops':
        print("Creating senior devops")
        return senior_devops(llm)
    else:
        return None

def senior_developer(llm):
    return Agent(
        role='Senior Developer',
        goal='Develop code that is high quality, scalable, and maintainable.',
        backstory="""You are a senior developer with 10 years of experience. 
        You have worked on a variety of projects and have a deep understanding of software development best practices. 
        You are passionate about writing clean, efficient code and am always looking for ways to improve my skills.
        """,
        verbose=True,
        # You can pass an optional llm attribute specifying what model you wanna use.
        # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
        llm=llm
    )
 
def senior_devops(llm):
    return Agent(
        role='Senior DevOps Engineer',
        goal='Make sure the code works repeatably and is idempotent.',
        backstory="""You are a senior Devops Engineer with 10 years of experience.
        You write a lot of bash scripts as you live in the terminal all day.`
        """,
        verbose=True,
        llm=llm
        # You can pass an optional llm attribute specifying what model you wanna use.
        # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
    )
