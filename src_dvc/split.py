import yaml


if __name__ == "__main__":
    with open("params.yaml", "r") as fd:
        params = yaml.safe_load(fd)

    print(f"Here we can set seed: {params['split']['seed']}")

    with open("resources/data.txt", "r") as f:
        x = f.readline().strip()
        y = f.readline().strip()

    with open("resources/train.txt", "w") as f:
        f.write(x[1::2])
        f.write("\n")
        f.write(y[1::2])

    with open("resources/test.txt", "w") as f:
        f.write(x[0::2])
        f.write("\n")
        f.write(y[0::2])