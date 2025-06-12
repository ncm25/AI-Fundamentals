## 🛠️ Prerequisites

Before starting this course, please make sure you meet the following requirements. These steps will help you get the most out of each session and allow you to follow along with all the hands-on exercises:

### 1. Python Installation
- Install **Python 3.12** or above.  
  [Download Python here](https://www.python.org/downloads/)

### 2. Code Editor
- Install a code editor such as **VSCode** (recommended) or **PyCharm**.
  - [Download VSCode](https://code.visualstudio.com/)
  - [Download PyCharm](https://www.jetbrains.com/pycharm/download/)

### 3. Jupyter Notebook
- Install **Jupyter Notebook** (via Anaconda, Miniconda, or pip).
  - [Jupyter installation guide](https://jupyter.org/install)

### 4. Create a Virtual Environment
- Set up a **virtual environment** for your Python projects (using `venv`, `virtualenv`, or `conda`).
  
  - Example for Windows:
    ```powershell
    python -m venv ai-course-env
    .\ai-course-env\Scripts\activate
    ```

  - Example for Linux/Mac:
    ```bash
    python3 -m venv ai-course-env
    source ai-course-env/bin/activate
    ```

### 5. Directory Structure (Best Practices)
- Use this recommended structure for your projects:
    ```
     ai_python_course/
     ├── notebooks/
     ├── data/
     ├── src/
     ├── results/
     ├── README.md
     └── requirements.txt
     ```
- **notebooks/**: Jupyter notebooks for each session  
- **data/**: Datasets used in the course  
- **src/**: Python scripts (functions, utilities, experiments)  
- **results/**: Output files, figures, and models  
- **README.md**: Your course notes and documentation  
- **requirements.txt**: List of required Python packages

### 6. Required Python Packages
- Install the following packages in your virtual environment:
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn jupyter
    ```
  *(Additional packages will be introduced as needed in the course, such as `tensorflow`, `torch`, or `opencv`.)*
- Or, Install dependencies using the provided `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```
     
### 7. Basic Command Line Usage
- Be comfortable navigating folders and running commands in the terminal (Command Prompt, PowerShell, or Terminal).

### 8. Recommended: Git (Optional, but useful!)
- Install **Git** for version control and good development practices.
  - [Download Git](https://git-scm.com/downloads)

---

**No previous experience with AI or advanced programming is required! If you have any questions or need help with setup, feel free to reach out before the first session.**


---

## ⚡ Quick Setup Guide

We provide automation scripts and a Makefile to make your setup as easy as possible.  
**Most students use Windows 11 — follow the first set of instructions. Linux/Mac users, see below.**

### 1. Download or Clone the Repository

Download or clone this repository to your computer:
```bash
git clone https://github.com/arojaspa76/AI-Fundamentals.git
cd ai_python_course
```

### 2. Create the Folder Structure Automatically
For Windows 11 (PowerShell):
- Open PowerShell in the folder where you want your project.
- Run:
```bash
.\setup_ai_course.ps1
```
*Note: If you get a permissions error, run as administrator the following:*
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

For Linux/Mac:
- Open your terminal.
- Run:

```bash
bash setup_ai_course.sh
```
This will create the recommended folders and template files (README.md, requirements.txt, Makefile).
---
