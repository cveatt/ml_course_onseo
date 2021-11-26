import requests


if __name__ == "__main__":
    response = requests.get("http://127.0.0.1:8000/api/v1/health")

    print(response.status_code)
    print(response.json())


    response = requests.post(
        "http://127.0.0.1:8000/api/v1/predict",
        json={"text": "Nice day."}
    )

    print(response.status_code)
    print(response.json())