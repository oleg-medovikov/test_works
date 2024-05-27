import pandas as pd


def main():
    filename = "tmp/f.txt"
    df = pd.read_csv(filename, sep="|")

    unique_records = df.drop_duplicates(subset="id", keep=False)
    print(f"Уникальные записи:\n {unique_records}")

    duplicate_records = df[df.duplicated(subset="id", keep=False)]
    print(f"\nЗаписи с одинаковыми id, но разными данными:\n {duplicate_records}")


if __name__ == "__main__":
    main()
