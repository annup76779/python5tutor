# " ".join(["anurag", "pandey"])

def concate_for_me(sq, *, sep = " ", is_str = True, ends_with = "") -> str:
	assert isinstance(sq, (list, tuple))
	# I have to teach you how to check if all the data in list is of specific type
	assert all(isinstance(x, str) for x in sq)
	# if assert is True, code works else AssertionError will be raised
	assert isinstance(sep, str) # seperator must be string
	if is_str:
		res = sep.join(sq)
		return res + ends_with
	else:
		res = sep.join([str(sq_Data) for sq_Data in sq])
		return res + ends_with

print(concate_for_me(["Anurag", 1], sep = " 5 ", ends_with = " is fine coder."))

