# Human Verification & Confession App

This is a Flask-based web application featuring a CAPTCHA verification step followed by a "Seven Deadly Sins" validation page.

## Prerequisites
* Python 3.7 or higher installed on your system.

## Setup Instructions

To keep dependencies isolated, it is highly recommended to run this application inside a Python virtual environment (`venv`). 


### 1. Open your terminal or command prompt
Navigate to the directory containing `app.py` and `requirements.txt`.


### 2. Create the Virtual Environment
Run the following command to create a folder named `venv` that will hold your isolated Python environment:
```bash
python -m venv venv
```


### 3. Activate the Virtual Environment

* Windows (Command Prompt):
```bash
python -m venv venv
```

* Windows (PowerShell):
```bash
venv\Scripts\Activate.ps1
```

* macOS / Linux:
```bash
source venv/bin/activate
```


### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
python app.py
```

### 6. Access the App
 Open your web browser and go to:
 `http://127.0.0.1:5000`

### Deactivating

When you are done, you can exit the virtual environment by typing:

`deactivate`
