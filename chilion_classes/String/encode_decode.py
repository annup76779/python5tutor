str1 = "I am Anurag."

# encoding -> it is used to solve sometimes compatibility issues with computer or other devices.
str2 = str1.encode("utf32")

print(str2)

# decoding -> it is the resipocle of the encoding(). it return back a string to the format which human beings can understand.

str3 = str2.decode("utf32")
print(str3)