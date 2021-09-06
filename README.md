# Welcom to FastAPI course.

## Ref: [FastAPI](https://fastapi.tiangolo.com/)
![alt text](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png "Logo")

## Editor and Tools
* [Python interpreter](https://www.python.org/downloads/)
* [Video: install python on windows 10](https://www.youtube.com/watch?v=UvcQlPZ8ecA)
* [VSCode](https://code.visualstudio.com/)
* [Video: How to install VScode](https://www.youtube.com/watch?v=ApMDPi06DGM&list=PLoTScYm9O0GEo8pnhJb-m-MGVGDvGb4bB&index=2)
* [Post-man](https://www.postman.com/downloads/)

## Extension ส่วนเสริม สำหรับ VS Code
* [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
* [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)

## Course Outline
* FastAPI คืออะไร
    * ทำงานอย่างไร
    * ผู้สร้าง FastAPI
    * ประสิทธิภาพ (Performance)

* RESTFul API
    * What's RESTFul
    * How dose it work

* Install and Setup Tools.
    * Install Python
    * Install Vscode
    * Install Extension

* Setup Project
    * Install FastAPI
        * `pip install fastapi`
        * `pip install uvicorn[standard]`
    * Run FastAPI
        `uvicorn main:app --reload`

* Hello World FastAPI
    * GET
        * create route and return `Hello World`
        * create route for ice_cream and request 'id' for parameter

    * Introduce Redoc and Docs (Swagger UI)
    * Introduce BaseModel
    * create PUT ice_cream and adapt BaseModel
