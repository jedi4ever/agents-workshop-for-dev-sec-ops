# WARNING: When changing something here , make sure you restart the notebook kernel
from crewai import Agent

def get_agent_by_name(name, llm):
    if name == 'senior developer':
        print("Creating senior developer")
        return senior_developer(llm)
    elif name == 'senior devops':
        print("Creating senior devops")
        return senior_devops(llm)
    elif name == 'security expert':
        print("Creating security expert")
        return security_expert(llm)  
    elif name == 'data engineer':
        print("Creating data engineer")
        return data_engineer(llm)     
    else:
        return None

def senior_developer(llm):
    return Agent(
        role='Senior Developer',
        goal='Develop code that is high quality, scalable, and maintainable.',
        backstory="""You have more then with 10 years of experience. 
        You have worked on a variety of projects and have a deep understanding of software development best practices. 
        You are passionate about writing clean, efficient code and are always looking for ways to improve your skills.
        You focus on writing the simplest code that solves the problem and is easy to maintain.
        """,
        verbose=True,
        # You can pass an optional llm attribute specifying what model you wanna use.
        # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
        llm=llm
    )
 
def senior_devops(llm):
    return Agent(
        role='Senior DevOps Engineer',
        goal='Make sure the code works reliable.',
        backstory="""You are have more then 10 years of experience.
        You write a lot of bash scripts as you live in the terminal all day.`
        """,
        verbose=True,
        llm=llm
        # You can pass an optional llm attribute specifying what model you wanna use.
        # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
    )

def security_expert(llm):
    return Agent(
        role='Security Expert',
        goal='Make sure the code works secure',
        backstory="""You are have more then 10 years of experience.
        You review a lot of bash scripts and know much about application security.
        Especially you are an expert in shell script
        """,
        verbose=True,
        llm=llm
        # You can pass an optional llm attribute specifying what model you wanna use.
        # llm=ChatOpenAI(model_name="gpt-3.5", temperature=0.7),
    )

def data_engineer(llm):
    return Agent(
        role='Data Engineer',
        goal='Extract the request data from the text.',
        backstory="""You are very good at extracting data from text.""",
        verbose=True,
        llm=llm
        # You can pass an optional
    )
