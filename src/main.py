from utils.json import load_json, save_json

DATA_PATH = "../data"

def main():
  #Example 1
  data = load_json(f"{DATA_PATH}/input/tests/example_1.json")
  save_json(data, f"{DATA_PATH}/output/tests/results.json")


if __name__ == "__main__":
    main()
