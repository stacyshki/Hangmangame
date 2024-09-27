counter = 0

def file_reading():
  word_dictionary = {}
  
  with open('words.txt', 'r') as file:
    
    for value in file:
      value = value[:-2]
      key = len(value)
      
      if key in word_dictionary.keys():
        word_dictionary[key].append(value.upper())
      else:
        word_dictionary[key] = [value.upper()]
  
  return word_dictionary
