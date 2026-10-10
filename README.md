# Todo API

A task management REST API built with FastAPI.

## Features

- Create tasks
- Retrieve tasks
- Update tasks
- Delete tasks

## Tech Stack

- Python
- FastAPI

## Installation

Create a virtual enviroment:

```
python -m venv .venv
```

Activate the virtual environment:

```
.venv\Scripts\Activate.ps1
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application

```
uvicorn app.main:app --reload
```

## Interactive API documentation

Open the interactive API documentation at http://127.0.0.1:8000/docs.