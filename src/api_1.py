import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .modules.api_data_models import Message, HouseInfo, HousePrice
from .modules.simple_ml_models import HousePriceModel


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


@app.post("/api/v1/predict", response_model=HousePrice, responses={**DEFAULT_RESPONSES})
def predict(house_info: HouseInfo):
    logger.info("Predict.")

    try:
        price = app.model(
            n_floors=house_info.n_floors, 
            area=house_info.area, 
            heating=house_info.heating,
        )
        return HousePrice(price=price)

    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(status_code=500, content={"message": str(exception)})