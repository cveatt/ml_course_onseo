import requests


BASE_URL = "http://127.0.0.1:8000/"


if __name__ == "__main__":
    resp = requests.get(BASE_URL + "api/v1/health")
    print(resp.status_code)
    print(resp.json())

    resp = requests.post(
        BASE_URL + "api/v1/predict", 
        json={"n_floors": 2, "area": 100, "heating": "B"}
    )
    print(resp.status_code)
    print(resp.json())
    