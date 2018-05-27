from random import randint

class RandomNaiveNamesIterator():
  """Naive generation of random "name" like Cyrillic strings  """

  def __init__(self, name_count, min_length, max_length):
    self.name_count = name_count
    self.min_length = min_length
    self.max_length = max_length
    self.count = 0

    self.vowels = ["а","о","е","и","ю","я"]

  def __get_random_consonant(self):
    s = chr(randint(1072, 1103))
    # we need only consonant, so loop until one is found
    while s in self.vowels:
      s = chr(randint(1072, 1103))
    return s

  def __get_random_vowel(self):
    return self.vowels[randint(0,4)]

  def __get_random_name(self):
    ### create random name, between min_length and max_length letters long:
    self.name = []
    self.name_length = randint(self.min_length,self.max_length)

    letter_functions = [self.__get_random_consonant, self.__get_random_vowel]

    for i in range(self.name_length):
      # give 50% - 50% chance for a vowel (not quite exact, but it's ok for demo):
      vowel_chance = randint(0,1)
      self.name.append( letter_functions[vowel_chance]() )

    self.name = "".join(self.name)

    return self.name.capitalize()

  def __iter__(self):
    return self

  def __next__(self):
    name = self.__get_random_name()

    if ( self.count < self.name_count):
      self.count += 1
      return name
    else:
      raise StopIteration

# make some "names":
for name in RandomNaiveNamesIterator(name_count=10, min_length = 3, max_length = 8):
  print(name)