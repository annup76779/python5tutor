import os
os.system('clear')
print()
def remove_extra_whitespaces(infile, outfile):
    with open(infile, 'r') as f:
        data = f.readlines()
    new_data = []
    prev_element = None
    for element in data:
        if element!='\n':
            element = " ".join(element.split())
            element+='\n'
        if element!=prev_element:
            new_data.append(element)
            prev_element=element
    print(new_data)
    with open(outfile, 'w') as of:
        of.writelines(new_data)
    




def adjust_linelength(infile, outfile):
    with open(infile, 'r') as f:
        data = f.readlines()
    print(data)
    new_data = []
    new_line = ''
    print("-"*20, "lines")
    for line in data:
        print(line)
        if line != '\n':
            new_line += line.replace('\n', ' ')
        else:
            new_data.append(new_line+'\n')
            new_data.append('\n')
            new_line = ''
    print("new Data: \n", new_data)
    result = []
    for line in new_data:
        new_line = line.split(' ')

        # print(new_line)
        max_char = 60
        res_line = ''
        for i in range(len(line)):
            if len(line[i])<max_char:
                res_line+=line[i]
                max_char-=len(line[i])
            else:
                res_line+='\n'+line[i].strip()
                max_char=60
        print(res_line)   
        result.append(res_line)
        
    print("result\n", result)
    with open(outfile, 'w') as of:
        of.writelines(result)



def essay_statistics(infile, outfile):
    non_blank_lines = 0
    with open(infile) as f:
        lines = f.readlines()

    for line in lines:
        if line!='\n':
            non_blank_lines+=1

    number_of_words = 0
    total_word_lengths = 0
    for line in lines:
        if line!= '\n':
            line = line.strip().split(' ')
            words_in_line = len(line)
            number_of_words+=words_in_line
            total_word_lengths+=len(''.join(line))

    average_word_length = total_word_lengths//number_of_words
    with open(outfile, 'a') as of:
        of.write(f"Number of (non-blank) lines: {non_blank_lines}\n")
        of.write(f"Number of words: {number_of_words}\n")
        of.write(f"Average word length: {average_word_length}\n")


def format_essay():
    print('''
    Essay Formatting Helper Program
    -------------------------------
    ''')
    file = "Enter the name (*.txt) of the file containing the essay: "
    remove_extra_whitespaces("essay.txt", "essay_neb.txt")
    adjust_linelength("essay_neb.txt", 'essay_final.txt')
    essay_statistics("essay_final.txt", "essay_stats.txt")
    
    
    print(
    '''
    Three files have been created:
    essay_neb.txt: the essay without extra whitespaces or blank lines
    essay_final.txt: the formatted essay
    essay_stats.txt: the essay statistics
    '''
    )
    
format_essay()
