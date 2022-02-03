# Partition -> The function partition() divides the string (say S) into two parts based on a delimter and return a tuples(next chaplter) 
# delimter means -> it can be considered as end of somethings.


# S = "Hello.Anurag.Pandey"

# print(S.partition("."))

# Split -> Tthe function split() enables us to split a string into a list of strings based on a seperator. 
# print(S.split("."))

sentence = input("Enter the sentence:\n")
print(sentence.strip())

word_list = sentence.split()
print(len(word_list))
print(word_list)

new_list = []
for i in word_list:
    new_list.append(i*2)

print(len(new_list))
new_sentence = " > ".join(new_list)
print(new_sentence)