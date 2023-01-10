def reverse(s):
    stack = []
    for ch in s:
        stack.append(ch)

    for _ in range(len(stack)):
        print(stack.pop(), end="")

    print(end=" ")


s = "This is Anurag Pandey"

word = ""
i = 0  # index of string
is_last_space = False  # in case the last character of the string was a space
while True:  # run it for infinite time
    ch = s[i]  # fetching the string character
    if ch == " ":
        if is_last_space:
            continue  # skip this iteration

        reverse(word)  # this will reverse the work of the string and print it on the screen
        word = ""
    else:  # if the current character is not a space
        if is_last_space:
            is_last_space = False  # make flag back to original state says last character is not a space.

        # if the current character is not space add current character to the word
        word += ch

    i += 1
    if i == len(s):
        reverse(word)
        break
