def main():

  number1 = 99
  number2 = 98

  for i in range (0,99) :
    print(str(number1) + " bottles of beer on the wall. " + str(number1) + " bottles of beer. Take one down, pass it around, " + str(number2) + " bottles of beer on the wall.")
    number1 = number1 - 1
    number2 = number2 - 1

    if (number1 == 2):
      print(str(number1) + " bottles of beer on the wall. " + str(number1) + " bottles of beer. Take one down, pass it around, " + str(number2) + " bottle of beer on the wall.")
      break

  print("1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.")
  print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")


main()