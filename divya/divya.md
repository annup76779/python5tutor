# Indexing
<p>
In python we have two types of indexing<br>

1. forward index(positive indexing)<br>
2. backward index(negative indexing)<br>

<b>Forward Indexing (positive indexing)</b> - It starts from 0 and goes to the length of the content(list, string, tuple, array, numpy.array, deque, etc.) minus 1.
<br>

<b>Backward Indexing (negative indexing)</b> - It starts from 1 * (-1) [or -1] and goes to the length of the content(list, string, tuple, array, numpy.array, deque, etc.) multiplied by -1.
</p>

# Slicing
<p>
Sometimes we need t retrieve a substring, also called a slice, from a string. This can be some by specifying an index range. <br><br>

This has 3 parts:<br><br>

1. starting index(positive/negative)<br>
2. ending index + 1 (positive/negative)<br>
3. skips(for me)/increments(by python) (positive/negative)<br>
<br>
<b>Increments in index range:</b> - It gets added to the last index which was printed or added to some objec or string.
</p>

<pre>
# Slicing simple example
str = 'abcdefghijklmnopqrstuvwxyz'

# want to get the first 10 alphabets
new_str = str[: 10]

# we want to get the last 10 alphabets
new_str2 = str[15 : ] 

# want to get the 5 to 13 alphabets
new_str3 = str[5: 14]

# want to get the 20 alphabets but 1 skipped in them
new_str4 = str[: 20: 2]

</pre>

# Strings Basic Builtins

1. count -> used to find the count of any substring present in the string.<br>
2. find -> find() actually finds any substring out of a string but it gives the index of the first substring in finds.<br/>
3. rfind -> rfind() actually finds any substring out of a string from right side of the string but it gives the index of the first substring in finds.<br/>
4. capitalize, title, lower, upper -> capitalize(), title(), lower(), upper()<br/>
5. islower, isuper, istitle -> islower(), isuper(), istitle()<br/>
6. replace() -> it is used to replace any thing is string with any other data. It actually returns a new string with updated data.

<font color="yellow"> 

<b>change Rule for a string:</b> It says that you cannot change any data in string, if you have to change any data in a string then you have to create a new string with changed value.

</font>