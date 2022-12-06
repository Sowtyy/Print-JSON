import json
import os
from time import sleep


class MyApp:
  version = "1.0.0"
  version_date = "11.05.2022 @ 9 pm"
  
  name = "Print JSON"

  sleep_time = 1
  run = True


defaultSpaces = "   "


def buildString(char : str, num : int):
  string = ""
  for i in range(num):
    string += char
  
  return string

# spacesX2 = buildString(spaces[0], len(spaces) * 2)

def printDict(dct : dict, spaces : str = defaultSpaces):
  for i, key in enumerate(dct):
    spacesX2 = spaces + defaultSpaces
    itm = dct[key]
    print(f"{spaces}{i + 1}: {key}", end = "")

    if type(itm) == dict:
      print()
      printDict(itm, spacesX2)
    elif type(itm) == list:
      print()
      printList(itm, spacesX2)
    else:
      print(f" - {itm}")

  print()
  return

def printList(lst : list, spaces : str = defaultSpaces):
  for i in range(len(lst)):
    spacesX2 = spaces + defaultSpaces
    itm = lst[i]
    print(f"{spaces}{i + 1}:", end = "")

    if type(itm) == dict:
      print()
      printDict(itm, spacesX2)
    elif type(itm) == list:
      print()
      printList(itm, spacesX2)
    else:
      print(f" - {itm}")

  print()
  return

def readFile(path : str):
  with open(path, "r") as f:
    return json.load(f)


def main():

  os.system(f"title {app.name} {app.version}  by Sowtyy")


  while app.run:
    inp = input("Enter JSON file location or /q to exit: ")

    if inp.lower() == "/q":
      app.run = False
      continue
    
    print("\n\n")

    try:
      fCont = readFile(inp)
    except Exception as e:
      print(repr(e))
      continue


    if type(fCont) == dict:
      printDict(fCont)
    elif type(fCont) == list:
      printList(fCont)
    else:
      print(fCont)

    #sleep(app.sleep_time)

  return


if __name__ == "__main__":
  app = MyApp()
  
  try:
    main()
  except Exception as e:
    print("-- error main:", repr(e))

  if app.run:
    input()
