# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas

df = pandas.read_csv("./csv_files_pandas_lib/projects/alphabet/nato_phonetic_alphabet.csv")

data_dict = {row.letter : row.code for (index, row) in df.iterrows ()}

# print (data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input ("Enter word: ").upper ()

code_words = [data_dict[letter] for letter in word]

print (code_words)

