import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.modules.simple_ml_models import SentimentModel

from .modules.api_data_models import Message, RequestText, ResponseSentiment


DEFAULT_RESPONSES = {
    500: {"model": Message},
}


logging.basicConfig(
    format="[%(asctime)s][%(name)s][%(levelname)s] ~ %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger()

app = FastAPI()
app.model = SentimentModel()


@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check.")

    return Message(message="Success.")


@app.post("/api/v1/predict", response_model=ResponseSentiment, responses={**DEFAULT_RESPONSES})
def predict(text: RequestText):
    logger.info("Sentiment.")

    try:
        sentiment = app.model(text=text.text)
        return ResponseSentiment(**sentiment)

    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(status_code=500, content={"message": str(exception)})