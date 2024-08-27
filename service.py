from pydantic import BaseModel
from uuid import uuid4
from typing import List

class Message(BaseModel):
    account_id: str
    message_id: str
    sender_number: str
    receiver_number: str
