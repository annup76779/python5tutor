

# pip install PyMuPDF

import fitz
from operator import itemgetter
import re
import pandas as pd
import os

import requests

def read_link(url:str, save_at:str):
    response = requests.get(url) # getting the file

    with open(save_at, "wb") as pdf:
        pdf.write(response.content)

    pdf.close()
    return save_at


def fonts(doc, granularity=False):
    """Extracts fonts and their usage in PDF documents.
    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param granularity: also use 'font', 'flags' and 'color' to discriminate text
    :type granularity: bool
    :rtype: [(font_size, count), (font_size, count}], dict
    :return: most used fonts sorted by count, font style information
    """
    styles = {}
    font_counts = {}

    for page in doc:
        blocks = page.getText("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b['type'] == 0:  # block contains text
                for l in b["lines"]:  # iterate through the text lines
                    for s in l["spans"]:  # iterate through the text spans
                        if granularity:
                            identifier = "{0}_{1}_{2}_{3}".format(s['size'], s['flags'], s['font'], s['color'])
                            styles[identifier] = {'size': round(s['size']), 'flags': s['flags'], 'font': s['font'],
                                                  'color': s['color']}
                        else:
                            identifier = "{0}".format(s['size'])
                            styles[identifier] = {'size': round(s['size']), 'font': s['font']}

                        font_counts[identifier] = font_counts.get(identifier, 0) + 1  # count the fonts usage

    font_counts = sorted(font_counts.items(), key=itemgetter(1), reverse=True)

    if len(font_counts) < 1:
        raise ValueError("Zero discriminating fonts found!")

    return font_counts, styles

url = "http://www.ph.ucla.edu/epi/rapidsurveys/RScourse/RSbook_ch3.pdf"
file = fitz.open("my_pdf.pdf")

font, style = fonts(file, granularity=False)
# print(font)




font_sizes = []
for (font_size, styles) in font:
    font_sizes.append(round(float(font_size.split("_")[0])))


font_sizes.sort(reverse = True)
p_size = style[font[0][0]]["size"]
print(style)
print(font)

idx = 0
size_tag = {}
for size in font_sizes:
    idx += 1
    if size == p_size:
        idx = 0
        size_tag[size] = '<p>'
    if size > p_size:
        size_tag[size] = '<h{0}>'.format(idx)
    elif size < p_size:
        size_tag[size] = '<s{0}>'.format(idx)

size_tag

def headers_para(doc, size_tag):
    """Scrapes headers & paragraphs from PDF and return texts with element tags.
    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param size_tag: textual element tags for each size
    :type size_tag: dict
    :rtype: list
    :return: texts with pre-prended element tags
    """
    header_para = []  # list with headers and paragraphs
    first = True  # boolean operator for first header
    previous_s = {}  # previous span

    for page in doc:
        blocks = page.getText("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b['type'] == 0:  # this block contains text

                # REMEMBER: multiple fonts and sizes are possible IN one block

                block_string = ""  # text found in block
                for l in b["lines"]:  # iterate through the text lines
                    for s in l["spans"]:  # iterate through the text spans
                        if s['text'].strip():  # removing whitespaces:
                            if first:
                                previous_s = s
                                first = False
                                block_string = size_tag[round(s['size'])] + s['text']
                            else:
                                if s['size'] == previous_s['size']:

                                    if block_string and all((c == "|") for c in block_string):
                                        # block_string only contains pipes
                                        block_string = size_tag[round(s['size'])] + s['text']
                                    if block_string == "":
                                        # new block has started, so append size tag
                                        block_string = size_tag[round(s['size'])] + s['text']
                                    else:  # in the same block, so concatenate strings
                                        block_string += " " + s['text']

                                else:
                                    header_para.append(block_string)
                                    block_string = size_tag[round(s['size'])] + s['text']

                                previous_s = s

                    # new block started, indicating with a pipe
                    # block_string += "|"

                header_para.append(block_string)

    return header_para

final = headers_para(file, size_tag)
while '<h1>APPROVED' in final:
    final.remove('<h1>APPROVED')

while '' in final:
    final.remove('')

print(final)

def export_data(final):
    exp = re.compile(r"^<\w+>")
    s = '<h3>'
    tags_val = {}
    is_last_one_heading = [False, ""]
    for item in final:
        match = re.match(exp, item)
        if match:

            tag = match.group()
            tag_name = tag[1]
            if tag_name == 'h':
                
                if is_last_one_heading[0]:
                    key += item[match.span()[1]:]
                    is_last_one_heading[1] += key
                else:
                    key = item[match.span()[1]:]
                    is_last_one_heading[1] = key
                tags_val[key]=""
            else:
                is_last_one_heading[0] = False
                key = is_last_one_heading[1]
                tags_val[key] += item[match.span()[1]:]


   
    df = pd.DataFrame(tags_val.items(), columns = ["Headings", "Descriptions"])
    df.to_csv(os.path.join(r"C:\Users\ANJU SHARMA\PycharmProjects\inthp", "Pdf_extract.csv"), index=False)
    print(df)
export_data(final)
# s = "<p>"
# s[1]

