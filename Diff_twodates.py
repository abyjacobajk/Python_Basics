import random
char_list = ['a','e','i','o','u']
random.shuffle(char_list)
print(''.join(char_list))

def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))
