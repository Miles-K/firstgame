def get_user_input():
  user_input = input()
  return user_input

def get_user_input_m(input_msg):
  user_input = input(input_msg)
  return user_input

if __name__ == "__main__":
  user_input = get_user_input()
  print("You entered:", user_input)