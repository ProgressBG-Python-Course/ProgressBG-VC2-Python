import pickle

# let's serialize a simple dict
prices = { 'apples': 2.50, 'oranges': 1.90, 'bananas': 2.40 }

#convert the object to a serialized string
serialized_prices = pickle.dumps( prices )
print(serialized_prices)

#de-serialize (unpickle) an object
received_prices = pickle.loads( serialized_prices )
print(received_prices)