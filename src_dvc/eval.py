import time
import json 

import yaml


if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)

    print(f"Here we can set seed: {params['eval']['seed']}")

    with open("resources/test.txt", "r") as f:
        x_test = f.readline().strip()
        y_test = f.readline().strip()

    print("Load model...")
    model = {}
    with open("resources/model.txt", "r") as f:
        inp = f.readline().strip()
        out = f.readline().strip()
    for i in range(len(inp)):
        model[inp[i]] = out[i]

    print("Eval...")
    score = 0
    for x, y in zip(x_test, y_test):
        score += int(model[x] == y)
    score /= len(x_test)

    with open("metrics.json", "w") as f:
        json.dump(
            {
                "test": {
                    "accuracy": score,
                }
            },
            f,
            indent=4,
        )
