# Welcome to FastAPI course.

## Ref: [FastAPI](https://fastapi.tiangolo.com/)

![alt text](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png "Logo")

[How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/#why-we-need-pep-8)

[FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)

[What is REST](https://restfulapi.net/)

## Editor and Tools

- [Python interpreter](https://www.python.org/downloads/)
- [Video: install python on windows 10](https://www.youtube.com/watch?v=UvcQlPZ8ecA)
- [VSCode](https://code.visualstudio.com/)
- [Video: How to install VScode](https://www.youtube.com/watch?v=ApMDPi06DGM&list=PLoTScYm9O0GEo8pnhJb-m-MGVGDvGb4bB&index=2)
- [Post-man](https://www.postman.com/downloads/)

## Extension ส่วนเสริม สำหรับ VS Code

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)

## Course Outline

- FastAPI คืออะไร

  - ทำงานอย่างไร
  - ผู้สร้าง FastAPI
  - ประสิทธิภาพ (Performance)

- RESTFul API

  - What's RESTFul
  - How dose it work

- Install and Setup Tools.

  - Install Python
  - Install Vscode
  - Install Extension

- Setup Project

  - Install FastAPI
    - `pip install fastapi`
    - `pip install uvicorn[standard]`
  - Run FastAPI
    `uvicorn main:app --reload`

- Hello World FastAPI

  - GET

    - create route and return `Hello World`
    - create route for ice_cream and request 'id' for parameter

  - Introduce Redoc and Docs (Swagger UI)
  - Introduce BaseModel
  - create PUT ice_cream and adapt BaseModel
  - Create fully RESTFul Operation (HTTP Methods)

- Router

  - setup file structure
  - import APIRouter
  - config APIRouter
  - create ice_creams router
  - create users router

- Tortoise Orm

  - [Doc](https://tortoise-orm.readthedocs.io/en/latest/#introduction)
  - [install tortoise-orm](https://tortoise-orm.readthedocs.io/en/latest/getting_started.html#installation)
  - Introduct tortoise-orm
  - install tortoise-orm
    `pip install tortoise-orm`
  - config
  - connect to SQLite

- CORS
  - [Doc](https://fastapi.tiangolo.com/tutorial/cors/)
  - what's CORS
  - import cors to project
  - implement to project
