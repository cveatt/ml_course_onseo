import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .modules.data_models import Message, RequestCalc, ResponseCalc


DEFAULT_RESPONSES = {
    500: {"model": Message},
}


logging.basicConfig(
    format="[%(asctime)s][%(name)s][%(levelname)s] ~ %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger()

app = FastAPI()


@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check.")

    return Message(message="Success.")


@app.post("/api/v1/sum", response_model=ResponseCalc, responses={**DEFAULT_RESPONSES})
def calculate_sum(sum_request: RequestCalc):
    logger.info("Sum.")

    try:
        result = sum_request.a + sum_request.b
        return ResponseCalc(result=result)

    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(status_code=500, content={"message": str(exception)})


@app.post("/api/v1/div", response_model=ResponseCalc, responses={**DEFAULT_RESPONSES})
def calculate_div(sum_request: RequestCalc):
    logger.info("Div.")

    try:
        result = sum_request.a / sum_request.b
        return ResponseCalc(result=result)

    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(status_code=500, content={"message": str(exception)})