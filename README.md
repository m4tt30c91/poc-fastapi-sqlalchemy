# POC - FastAPI integration with SQLAlchemy

The following project is a minimal POC to demostrate the integration with the current latest version of FastAPI (0.103.2) with the current latest version of SQLAlchemy (2.0.22)

## Dependencies

The following project is dependant to:
- FastAPI
- SQLAlchemy (asyncio)
- SQLLite (asyncio)
- Uvicorn

## Running the code

You can simply run the POC wit uvicorn:

```
uvicorn poc-fastapi-sqlalchemy.main:app --reload
```

You can then interact with the application by going to:

```
http://localhost:8000/docs
```

## Project structure

The POC is a simple, minimalist, single module application with the following:
- main.py: module base, containing the FastAPI service definition
- database.py: database connectivity definition
- user.py: create / read service to showcase the POC project
- model.py: the data model definition for the persistence storage
- schema.py: the DTOs to interact with the REST interface
- service.py: a simple service layer (with some overlapping with the persistence layer)