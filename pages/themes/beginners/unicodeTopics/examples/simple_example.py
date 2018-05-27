""" TODO : does not work!!! """
string_to_decode = "Ива Попова"
output_file = "decoded_cp1251.txt"


with open(output_file, "w") as fh:
  # fh.writelines(string_to_decode+"\n")

  bytes_decoded = string_to_decode.encode()
  print(bytes_decoded)

  decoded_string = bytes_decoded.decode(encoding="cp1251")

  # fh.write(decoded_string)

