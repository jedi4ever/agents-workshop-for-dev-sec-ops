# WARNING: When changing something here , make sure you restart the notebook kernel

import tempfile
import subprocess
import os

def bash_validate(code: str) -> str:
    """Check if the code is valid bash code"""

    (valid, _err) = bash_valid(code)
    if (bash_valid(code)):
        return "The code is valid bash code"
    else:
        return "The code is not valid bash code"
    ## Write code to a tempfile and run it

def bash_valid(code: str) -> bool:
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write(code)
        temp_file = f.name

        try:
            result=subprocess.run(["bash","-n",temp_file], check=True)
            if (result.returncode != 0):
                return False 
            else:
                return True
        except subprocess.CalledProcessError as e:
            return False
            #return f"The code is not valid bash code\n{e}"
        finally:
            #print("removing temp file " + temp_file)
            os.remove(temp_file)

def markdown_validate(code: str) -> str:
    """Check if the code is valid markdown"""
    if (markdown_valid(code)):
        return "The code is valid markdown"
    else:
        return "The code is not valid markdown code block"
    
def markdown_valid(code: str) -> bool:
    if (code.startswith("```bash") and code.endswith("```")):
        return True
    else:
        return False    