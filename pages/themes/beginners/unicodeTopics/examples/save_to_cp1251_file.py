# string_to_decode = "Ива Попова"
input_file="test.utf8"
output_file = "test.cp1251"

# read UTF8 input:
with open(input_file, "r") as fi:
  string_to_decode = fi.read()
  print(string_to_decode)

  #decode to cp1251:
  bytes_decoded = string_to_decode.encode()
  # decoded_string = bytes_decoded.decode(encoding="koi8_r",errors="replace")
  decoded_string = bytes_decoded.decode(encoding="cp1251")
  print(decoded_string)

with open(output_file, "w", encoding="cp1251") as fo:
  fo.write(decoded_string)

