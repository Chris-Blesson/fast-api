from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pymysql

app = FastAPI()

# Database configuration
database_config = {
    "host": "127.0.0.1",
    "user": "your_username",
    "password": "your_password",
    "database": "your_db_name",
}

# Database connection
connection = pymysql.connect(**database_config)

# Create a table if it doesn't exist
with connection.cursor() as cursor:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT
    )
    """
    cursor.execute(create_table_query)

# Pydantic model for request data
class User(BaseModel):
    name: str
    age: int

# API endpoint to insert user into the database
@app.post("/users/")
async def create_user(user: User):
    with connection.cursor() as cursor:
        # Insert user into the database
        insert_query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        cursor.execute(insert_query, (user.name, user.age))
        connection.commit()

    return {"message": "User created successfully"}

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application with Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
