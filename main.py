import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data, type(data))
nato_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}


# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def func_loop():
    user_input = input("Enter a word:\n").upper()
    try:
        output_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only input letters please\n")
        func_loop()
    else:
        print(f"{output_list}")


func_loop()
