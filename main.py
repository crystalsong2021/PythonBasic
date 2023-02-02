from collections import Counter
def hashMap(string):
  return Counter(string)
  
s = "mountain"
result = hashMap(s)
print(result)