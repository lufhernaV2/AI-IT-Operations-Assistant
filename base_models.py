from pydantic import BaseModel
from typing import Literal

class Ticket(BaseModel):
    id: int
    description: str
    priority: Literal["Low", "Medium", "High"]