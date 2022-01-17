import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data, type(data))
nato_dict = {
    row.letter: row.code for (index, row) in data.iterrows()
}
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("What letters do you want to convert?\n").upper()
output_list = [nato_dict[letter] for letter in user_input]
print(output_list)