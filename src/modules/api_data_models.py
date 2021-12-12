from pydantic import BaseModel


class Message(BaseModel):
    message: str


class RequestCalc(BaseModel):
    a: float
    b: float


class ResponseCalc(BaseModel):
    result: float


class RequestHouseParams(BaseModel):
    area: float
    heating: str
    n_floors: int


class ResponseHousePrice(BaseModel):
    price: float


class RequestText(BaseModel):
    text:str


class ResponseSentiment(BaseModel):
    sentiment: str
    score: int