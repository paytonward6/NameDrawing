name = "Payton"
bin_name = []
for i in name:
    bin_name.append(str(format(ord(i), '08b')))
print(bin_name)
