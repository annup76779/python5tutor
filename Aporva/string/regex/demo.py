if __name__ == "__main__":
    import re

    s = "<h1>Introduction</h1><p>Regex is used to find a search pattern in a string.</p>"


    # \w means 

    exp1 = re.compile(r"<\w+>")
    exp2 = re.compile(r"</\w+>")

    match = re.findall(exp1, s)
    print(match)

    closing_match  = re.findall(exp2, s)
    print(closing_match)
    print(__name__)