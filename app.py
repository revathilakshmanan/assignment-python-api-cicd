from fastapi import FastAPI, HTTPException
from typing import Optional
import uuid

app = FastAPI()

messages_db = []  # In-memory store; switch to PostgreSQL with an ORM like SQLAlchemy in production.

@app.get("/get/messages/{account_id}")
def get_messages(account_id: str):
    result = [msg for msg in messages_db if msg['account_id'] == account_id]
    if not result:
        raise HTTPException(status_code=404, detail="No messages found for this account")
    return result

@app.post("/create")
def create_message(message: Message):
    message.message_id = str(uuid4())
    messages_db.append(message.dict())
    return {"status": "Message created", "message": message}

@app.get("/search")
def search_messages(message_id: Optional[str] = None, sender_number: Optional[str] = None, receiver_number: Optional[str] = None):
    result = messages_db
    if message_id:
        result = [msg for msg in result if msg['message_id'] in message_id.split(",")]
    if sender_number:
        result = [msg for msg in result if msg['sender_number'] in sender_number.split(",")]
    if receiver_number:
        result = [msg for msg in result if msg['receiver_number'] in receiver_number.split(",")]
    return result
