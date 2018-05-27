win1251file = "windows-1251_encoded_file.txt"
utf8file = "utf8_encoded_file.txt"

with open(win1251file, "r") as f:
  for line in f:
    print(line)