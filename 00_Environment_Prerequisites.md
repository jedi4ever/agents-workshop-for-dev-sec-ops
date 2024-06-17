## Setting up the Jupyter running environment with VSCode

### Get the Repo

> [!NOTE]
> You need to have git installed to clone the repo
> (alternatively, you could download the zip file)

Clone the workshop repository
```
git clone https://github.com/jedi4ever/agents-workshop-for-dev-sec-ops.git
```

### Configure VSCode
> [!Note]
> You need to have VSCode [installed](https://code.visualstudio.com/download)

Open VSCode

Click Code -> Settings -> Extensions 

Install the most popular VSCode extensions for Jupyter and Python

### Set up Python virtual environment

> [!Note]
> We want to create a virtual environment to keep the Python libraries installation local to our working folder (otherwise we might run into either version or permissions issues with the OS)

Click File -> Open Folder... and open the workshop repo directory

Open the *0_welcome.ipynb* file in the VSCode Editor

Click Select Kernel in the top right corner -> Select Another Kernel
![image](https://github.com/jedi4ever/agents-workshop-for-dev-sec-ops/assets/6864212/28a7f57d-eda5-4706-a12b-47503b5e42d4)

Click Python Environments -> Create Python Environment -> Venv -> Pick Python 3.12.3 (or your most recent version)

> You may get an error about pip not being available

Open Terminal in VSCode (or Terminal in your repo directory) and run the following two commands:

```
. ./.venv/bin/activate

pip install ipykernel
```

### Get an OpenAI API Key
Log into OpenAI and go to [API-key page](https://platform.openai.com/api-keys) to create a new API Key. 

Copy your API key and paste it into your .env_sample file 

Rename the .env_sample to .env

### Run

Now you should be able to run the notebooks inside the workshop files by clicking the Execute button
![image](https://github.com/jedi4ever/agents-workshop-for-dev-sec-ops/assets/6864212/2d92d0fd-f9f2-4ae6-890f-9f02d289b0fc)


