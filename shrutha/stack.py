def max_time_solution():
    def reverse(s):
        stack = []
        for ch in s:  # ----------------------  m
            stack.append(ch)

        for _ in range(len(stack)): # ----------------------  m
            print(stack.pop(), end="")

        print(end=" ")


    s = "This is Anurag Pandey"  # n

    word = ""
    i = 0  # index of string
    is_last_space = False  # in case the last character of the string was a space
    while True:  # run it for infinite time        # ----------------------  n
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

    # this is the maximum time taking solution for this
    # O(n.(4 * 2m))  ->  O(n. 8m)  8m ~ n   ->    < O(n2)  approximately


def average_time_solution():
    def reverse(s):
        for i in range(len(s)-1, -1, -1):
            print(s[i], end="")

        print(end=" ")

    s = "This is Anurag            Pandey"  # n

    word = ""
    i = 0  # index of string
    is_last_space = False  # in case the last character of the string was a space
    while True:  # run it for infinite time        # ----------------------  n
        ch = s[i]  # fetching the string character
        if ch == " ":
            if not is_last_space:
                is_last_space = True

                reverse(word)  # this will reverse the work of the string and print it on the screen
                # print(word[::-1], end=" )
                word = ""
        else:  # if the current character is not a space
            if is_last_space:
                is_last_space = False  # make flag back to original state says last character is not a space.

            # if the current character is not space add current character to the word
            word += ch

        i += 1
        if i == len(s):
            reverse(word)
            # print(word[:: -1])
            break

    # this is the maximum time taking solution for this
    # O(n.(4 * m))  ->  O(n. 4m)  4m ~ n   ->    < O(n2)  approximately

average_time_solution()