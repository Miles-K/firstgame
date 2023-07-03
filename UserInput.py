def getUserInput():
  UserInput = input()
  return UserInput

def getUserInput_m(input_msg):
  UserInput = input(input_msg)
  return UserInput

if __name__ == "__main__":
  UserInput = getUserInput()
  print("You entered:", UserInput)