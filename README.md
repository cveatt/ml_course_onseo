# ml_course_onseo


docker run -it python:3.8 /bin/bash

docker build -t streamlit_service -f Dockerfile.streamlit .
docker run -p 5005:5000 streamlit_service

docker build -t fastapi_service -f Dockerfile.fastapi .
docker run -p 8001:8000 fastapi_service

docker build -t dev_ml_course -f Dockerfile.dev .

docker run -it -v C:/ml_course_onseo/:/app/ dev_ml_course /bin/bash
