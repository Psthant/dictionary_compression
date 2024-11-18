# Cleaning up punctuations
def clean(words, include_punctuation=True) -> list:
    holder  = []
    for word in words:
        # If wants to include punctuation as unique characters
        if include_punctuation:
            left_cleaned = word.lstrip("'\".,!?()[]{};:")
            right_cleaned = word.rstrip("'\".,!?()[]{};:")

            left_punctuation = word.replace(left_cleaned, '')
            right_punctuation = word.replace(right_cleaned, '')

            if left_punctuation and right_punctuation:  # The word is enclosed in punctuation, might as well treat it as a separate word
                holder.append(word)
            else:   # not enclosed
                if left_punctuation:
                    holder.append(left_punctuation)
                cleaned_word = word.strip("'\".,!?()[]{};:")
                holder.append(cleaned_word)          
                if right_punctuation:
                    holder.append(right_punctuation)      
        else:
            cleaned_word = word.strip("'\".,!?()[]{};:")
            holder.append(cleaned_word)
    return holder

# Initialisation
def get_positions(words: str, starting_index: int, position_dict: dict):    # The parameters starting_index and position_dict is to maintain the data over paragraphs, and could be neglegible if it's just one paragraph
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    i = 0
    end_index = starting_index              # In case none of the words go into the if statement below, so it just returns the original starting_index in that case
    for word in unique_words:
        if word not in position_dict.keys():    # Cannot use enumerate because of this if statement
            end_index = starting_index + i + 1
            position_dict[word] = end_index
            i += 1
    return position_dict, end_index

def compress(data, write_file_path):
    paragraphs = data.split('\n')   # Splitting up the newlines first before they got all mixed with spaces
    positions_with_newline = [] # This is just positions_dict but with newline support
    position_dict = {}
    starting_index = 0
    for paragraph in paragraphs:
        words = paragraph.split()
        words = clean(words)
        positions_dict, starting_index = get_positions(words, starting_index, position_dict)
        positions = []

        for word in words:
            positions.append(str(positions_dict[word]))
        
        positions_with_newline.append('0')  # This marks the end of each paragraph
        positions_with_newline.extend(positions)

    positions_with_newline = positions_with_newline[1:] # The first index is 0 during the loop so it has to be removed
    with open(write_file_path, "w") as file:
        file.write(','.join(positions_with_newline) + "\n" + "\n".join(positions_dict.keys()))

if __name__ == '__main__':
    mode = 'f' #input("Enter mode: ")
    if mode == "f":
        with open("data.txt", "r", encoding='utf-8') as file:
            data = file.read()
    else:
        data = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU, ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
    compress(data, 'compressed_by_task3.txt')