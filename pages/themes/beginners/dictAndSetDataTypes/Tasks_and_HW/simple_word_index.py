text = """There is no pain you are receding
A distant ship smoke on the horizon
You are only coming through in waves
Your lips move but I can't hear what you're saying
When I was a child
I caught a fleeting glimpse
Out of the corner of my eye
I turned to look but it was gone
I cannot put my finger on it now
The child is grown
The dream is gone
I have become comfortably numb."""

def make_index(words):
  words = text.split( )
  index = {}
  for w in words:
    if w in index:
      index[w] += 1
    else:
      index[w] = 1

  return index

# print the symbols in longest word in index:
def find_max_word_length(index):
  max_word_length = 0
  for key in index.keys():
    if max_word_length< len(key):
      max_word_length = len(key)

  return max_word_length

# print sorted by values
def display_index(index, max_word_length):
  for item in sorted(index.items(), key=lambda t:t[1], reverse=True):
    print("|{word:<{width}s}|{count:^5d}|".format(
      word=item[0], width=max_word_length, count=item[1]))

index = make_index(text)
max_word_length = find_max_word_length(index)
print("max_word_length", max_word_length)
display_index(index, max_word_length)