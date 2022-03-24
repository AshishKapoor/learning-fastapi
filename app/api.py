from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}

# Get -> Read Todo

todos = [{"id": "1", "activity": "Something"},
         {"id": "2", "activity": "Something New"}]


@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}


@app.get('/todo/{id}', tags=['todos'])
async def get_todo_item(id: int) -> dict:
    return {"data": todos[id]}

# Post -> Create Todo


@app.post('/todo', tags=['todos'])
async def post_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A todo has been added."
    }

# Put -> Update Todo


@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['activity'] = body['activity']
            return {
                "data": f"A todo with {id} has been updated."
            }
        return {
            "data": f"Todo with id number {id} was not found!"
        }

# Delete -> Delete Todo


@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo["id"])) == id:
            todos.remove(todo)
            return {
                "data": f"todo with id {id} has been removed."
            }
        return {
            "data": f"todo with id {id} was not found!"
        }
