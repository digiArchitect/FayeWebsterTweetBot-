import json
def equals(arr1,arr2):
  if(len(arr1) != len(arr2)):
    return False
  n = len(arr1)
  for x in range(1, n - 1):
    if arr1[x] != arr2[x]:
      return false
  return True
def changeData(dictionary):
  with open("data.json", "w") as outfile:
    json.dump(dictionary, outfile)
  

