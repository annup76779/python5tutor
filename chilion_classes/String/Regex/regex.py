# what is regualer express?

# regular expression are used to find matches of pattern in a string.
import re

s = "hey guys I am python developer and I am learing #regex to develop my #python #coding #creativity skill so that i can get a #job #earning."

exp = re.compile("[#]\w+")

res = exp.findall(s)
print(res)