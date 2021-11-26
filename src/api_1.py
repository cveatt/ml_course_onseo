import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.modules.simple_ml_models import HousePriceModel

from .modules.data_models import Message, RequestHouseParams, ResponseHousePrice


DEFAULT_RESPONSES = {
    500: {"model": Message},
}


logging.basicConfig(
    format="[%(asctime)s][%(name)s][%(levelname)s] ~ %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger()

app = FastAPI()
app.model = HousePriceModel()


@app.get("/api/v1/health", response_model=Message, responses={**DEFAULT_RESPONSES})
def health():
    logger.info("Health check.")

    return Message(message="Success.")


@app.post("/api/v1/house_price", response_model=ResponseHousePrice, responses={**DEFAULT_RESPONSES})
def house_price(house_params: RequestHouseParams):
    logger.info("Price.")

    try:
        price = app.model(
            area=house_params.area,
            n_floors=house_params.n_floors, 
            heating=house_params.heating,
        )
        return ResponseHousePrice(price=price)

    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(status_code=500, content={"message": str(exception)})
