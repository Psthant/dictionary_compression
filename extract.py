PUNCTUATION = "'\".,!?()[]{};:\n"

def extract(read_file_path, write_file_path):
    with open(read_file_path, "r") as file:
        lines = file.readlines()

    compressed_str = lines.pop(0)
    indices = {i + 1: key.rstrip("\n") for i, key in enumerate(lines)}

    reconstructed_words = []
    for num in compressed_str.split(','):
        num = int(num)
        if num == 0:
            reconstructed_words.append('\n')
        else:
            reconstructed_words.append(indices[num])

    original = "\n"
    for word in reconstructed_words:
        if word in PUNCTUATION:
            if word == "":
                original += " "
            else:
                original += word
        else:
            if original[-1] == '\n':
                original += word
            else:
                original += " " + word
    original = original[1:]
    with open(write_file_path, 'w') as file:
        file.write(original)

if __name__ == '__main__':
    extract('compressed_by_task3.txt', 'extracted_from_task3.txt')