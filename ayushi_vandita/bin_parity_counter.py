bin_ = input("Enter the binary: ")

parity_count = 0 # counting identity is 0

for bit in bin_:
    if int(bit):
        parity_count += 1

print(parity_count)