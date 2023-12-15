from src.lab7 import calculate_maximum_chain, read_from_file

if __name__ == "__main__":
    with open("wchain.out", "w") as file:
        count, words = calculate_maximum_chain(*read_from_file('wchain.in'))
        file.write(f"result: {str(count)}\n")
        file.write(str(words))
