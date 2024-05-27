import pandas as pd


def main():
    a = [[1, 2, 3], [4, 5, 6]]

    # наверно подразумевается, что мы все равно используем пандас в проекте
    b = pd.DataFrame(a, columns=["k1", "k2", "k3"]).to_dict("records")
    print(b)


if __name__ == "__main__":
    main()
