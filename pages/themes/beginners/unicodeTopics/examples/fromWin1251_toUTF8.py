input_file_name = "windows-1251_encoded_file.txt"
output_file_name = "utf8_encoded_file.txt"


def decode_from(enc, file_name):
  # open file for read in bytemode
  with open(file_name,"rb") as f:
    content_in_bytes = f.read()
    decoded_content = content_in_bytes.decode(enc)

  return decoded_content

def encode_to(enc, content, file_name):
  # encode content:
  encoded_content = content.encode(enc)
  # open a file in byte write mode:
  with open(file_name,"wb") as f:
    f.write(encoded_content)


decoded_content = decode_from("cp1251", input_file_name)
encode_to("iso8859_5", decoded_content, output_file_name)


