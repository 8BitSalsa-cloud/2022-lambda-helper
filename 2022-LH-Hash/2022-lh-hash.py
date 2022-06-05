import hashlib

# data
example_data = ' Hallo, here are some data. whoop, whoop'

# function
def _hash_data_creation(example_data):
    hash_daten = hashlib.sha256(example_data.encode('utf-8')).hexdigest()
    return hash_daten

# check
print('This is the hash of the data creation: {}'.format(_hash_data_creation(example_data)))
# logger.debug('This is the hash of the data creation: {}'.format(_hash_data_creation(example_data)))
