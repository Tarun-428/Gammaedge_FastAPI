import subprocess
import sys
import os




# ANSI Escape Codes for Colors
class Col:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def check_version():
    version = sys.version
    print("Python Version :",Col.GREEN,version,Col.RESET)
    if 3.08 < float(version[:4]):
        print(f"{Col.GREEN}\t\t  version is greater than 3.8{Col.RESET}")
    else:
        print(f"{Col.RED}Version is less than 3.8 update ASAP!{Col.RED}")

def create_structure(project_name):
    dirs = ['src','test','docs','logs']
    try:
        for folder in dirs:
            path = os.path.join(project_name,folder)
            os.makedirs(path, exist_ok=True)
            print(f"{Col.UNDERLINE}Created {path}{Col.RESET}")
    except Exception as e:
        print(f"{Col.RED} Exception Occurred {e} {Col.RESET}")
def create_venv(project_name):
    env_name = "venv"
    venv_path = os.path.join(project_name,env_name)
    if os.path.exists(venv_path):
        print(f"{Col.UNDERLINE}Venv already present!{Col.RESET}")
        return
    try:
        subprocess.check_call([sys.executable,"-m","venv",venv_path])
        print(f"{Col.GREEN}virtual environment created successfully!{Col.RESET}")
    except Exception as e:
        print(f"{Col.RED} Exception Occurred {e} {Col.RESET}")

def generate_requirement(project_name):
    libraries = ['numpy','pandas','fastapi','sqlalchemy','tqdm','uvicorn','httpx']
    file_path = f'{project_name}/requirements.txt'
    directory = os.path.dirname(file_path)

    if not os.path.exists(directory):
        os.makedirs(directory,exist_ok=True)
    try:
        with open(file_path,'a') as f:
            for library in libraries:
                f.write(f"\n{library}")
        print(f"{Col.GREEN}Requirements.txt created successfully in {project_name}!{Col.RESET}")
    except Exception as e:
        print(f"{Col.RED} Exception Occurred {e} {Col.RESET}")

def create_gitignore(project_name):
    patterns = ['__pycache__/','.venv/','venv/','.env/','env/','build','.env','downloads/']
    file_path = f"{project_name}/.gitignore"
    directory = os.path.dirname(file_path)

    if not os.path.exists(directory):
        os.makedirs(directory,exist_ok=True)
    try:
        with open(file_path,'a') as f:
            for pattern in patterns:
                f.write(f"\n{pattern}")

        print(f"{Col.GREEN}.gitignore added successfully in {project_name}{Col.RESET}")
    except Exception as e:
        print(f"{Col.RED} Exception Occurred {e} {Col.RESET}")

def activate_venv(project_name):
    # venv_python = os.path.join("venv", "bin", "python")
    # subprocess.run([venv_python, "test.py"])
    command = f". venv/bin/activate && pip install -r {project_name}/requirements.txt && uvicorn main:app --reload"
    try:
        subprocess.run(command, capture_output=True,text=True,shell=True)

        # p = subprocess.Popen("source venv/bin/activate", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,shell=True,executable="/bin/bash")
        # output, errors = p.communicate()
        # print(output,errors)
    except KeyboardInterrupt:
        print(f"{Col.UNDERLINE}Program Stopped!{Col.RESET}")
    except Exception as e:
        print(f"{Col.RED}Exception occurred {e}{Col.RESET}")

def print_report():
    # Header
    print(f"{Col.BOLD}{Col.HEADER}   SYSTEM STATUS SUMMARY REPORT   {Col.RESET}")
    print(f"Date: 2026-01-29 | User: Admin\n")

    check_version()
    name = input(f"{Col.CYAN}Enter Project Name : ")
    Col.RESET
    print(f"{Col.YELLOW}Creating structure folder.....{Col.RESET}")
    create_structure(name)
    print(f"{Col.GREEN}Created structure folder Successfully!{Col.RESET}")
    print(f"{Col.YELLOW}Creating virtual environment .....{Col.RESET}")
    create_venv(name)
    print(f"{Col.YELLOW}Creating Requirements.txt .....{Col.RESET}")
    generate_requirement(name)
    print(f"{Col.YELLOW}Creating .gitignore .....{Col.RESET}")
    create_gitignore(name)
    activate_venv(name)
    print(f"{Col.BOLD}{Col.CYAN}All Task are executed Successfully!{Col.RESET}")
print_report()
