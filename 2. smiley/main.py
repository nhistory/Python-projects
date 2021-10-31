def main():
  # print first smiley
  print(":)")

  # value check for input
  try:
    space = int(input("How many characters would you like to move :)? "))
  except ValueError:
    print("x(  [Your input killed :)]")
    return

  # check the range of characters
  if ((space <= 0) or (space > 40)):
    print("x(  [Your input killed :)]")

  else:
    smiley = ":)"
    space = space + 2
    formater = "%" + str(space) + "s"
    print(formater % smiley)



main()