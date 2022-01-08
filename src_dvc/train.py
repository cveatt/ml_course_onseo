import time

import yaml


if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)

    print(f"Here we can set seed: {params['train']['seed']}")

    with open("resources/train.txt", "r") as f:
        x = f.readline().strip()
        y = f.readline().strip()

    print("Smth difficult...")
    time.sleep(10)
    d = {}
    for _x, _y in zip(x, y):
        d[_x] = d.get(_x, 0) + (1 if int(_y) else -1)

    print(d)

    print("Save model...")

    with open("resources/model.txt", "w") as f:
        inp = ""
        res = ""
        for el, val in d.items():
            inp += el
            if params['train']['positive_zero']:
                res += "1" if val >= 0 else "0"
            else:
                res += "1" if val > 0 else "0"

        f.write(inp)
        f.write("\n")
        f.write(res)
