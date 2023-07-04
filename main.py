'''
Can anyone tell how I can solve this question?
by using "if else statement", no function or any other thing.

Write a Python script to find out how many notes of
Rs. 2000, 500, 200, 100, 50, 20, 10, 5, 2, 1
and coins of 50 and 25 Paise would make up a given
amount of money assuming that the total amount would
be covered through the denominations of the highest
possible currency. For example, if the amount is
Rs. 10000 then it would be made up of 5 five
Rs. 2000 currency notes. Take any amount as test
case for solving this problem example Rs. 23950.75.
'''

'''
Function main()
'''
def main():
  samples = [23950.75, 20000.00, 5888.77]
  for sample in samples:
    make_change(sample)

'''
Function make_change()
'''
def make_change(amount):
  dlm = """
....+....|....+....|....+....|....+....|....+....|
  """
  print(dlm)
  denominations = [
    (2000.00, 0),
    ( 500.00, 0),
    ( 200.00, 0),
    ( 100.00, 0),
    (  50.00, 0),
    (  20.00, 0),
    (  10.00, 0),
    (   2.00, 0),
    (   1.00, 0),
    (   0.50, 0),
    (   0.25, 0),
    (   0.01, 0)]
  print(denominations)

  # amount = 23950.75
  print("amount:\n{:10.2f}".format(amount))

  while int(amount * 100) > 0:
  #   ix = 0
  #   while ix < len(denominations):
  #     if amount >= denominations[ix][0]:
  #       denominations[0] = (denominations[ix][0], denominations[ix][1] + 1)
  #       amount -= denominations[0][0]
  #       print("{:10.2f} - {:7.2f} - {:2d}".format(amount,
  #                                                 denominations[ix][0],
  #                                                 denominations[ix][1]))
  #     ix += 1

    if amount >= denominations[0][0]: # 2000.00
      denominations[0] = (denominations[0][0], denominations[0][1] + 1)
      amount -= denominations[0][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[0][0], denominations[0][1]))
  
    elif amount >= denominations[1][0]: # 500.00
      denominations[1] = (denominations[1][0], denominations[1][1] + 1)
      amount -= denominations[1][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[1][0], denominations[1][1]))
  
    elif amount >= denominations[2][0]: # 200.00
      denominations[2] = (denominations[2][0], denominations[2][1] + 1)
      amount -= denominations[2][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[2][0], denominations[2][1]))
  
    elif amount >= denominations[3][0]: # 100.00
      denominations[3] = (denominations[3][0], denominations[3][1] + 1)
      amount -= denominations[3][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[3][0], denominations[3][1]))
  
    elif amount >= denominations[4][0]: # 50.00
      denominations[4] = (denominations[4][0], denominations[4][1] + 1)
      amount -= denominations[4][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[4][0], denominations[4][1]))
  
    elif amount >= denominations[5][0]: # 20.00
      denominations[5] = (denominations[5][0], denominations[5][1] + 1)
      amount -= denominations[5][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[5][0], denominations[5][1]))
  
    elif amount >= denominations[6][0]: # 10.00
      denominations[6] = (denominations[6][0], denominations[6][1] + 1)
      amount -= denominations[6][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[6][0], denominations[6][1]))
  
    elif amount >= denominations[7][0]: # 2.00
      denominations[7] = (denominations[7][0], denominations[7][1] + 1)
      amount -= denominations[7][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[7][0], denominations[7][1]))
  
    elif amount >= denominations[8][0]: # 1.00
      denominations[8] = (denominations[8][0], denominations[8][1] + 1)
      amount -= denominations[8][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[8][0], denominations[8][1]))
  
    elif amount >= denominations[9][0]: # 0.50
      denominations[9] = (denominations[9][0], denominations[9][1] + 1)
      amount -= denominations[9][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[9][0], denominations[9][1]))
  
    elif amount >= denominations[10][0]: # 0.25
      denominations[10] = (denominations[10][0], denominations[10][1] + 1)
      amount -= denominations[10][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[10][0], denominations[10][1]))
  
    else: # 0.01
      denominations[11] = (denominations[11][0], denominations[11][1] + 1)
      amount -= denominations[11][0]
      print("{:10.2f} - {:7.2f} - {:2d}".format(amount, denominations[11][0], denominations[11][1]))

  print(denominations)
  check = 0.0
  for denom in denominations:
    if denom[1] != 0:
      print("{:2d} of {:7.2f} = {:10.2f}".format(denom[1], denom[0], denom[0] * denom[1]))
      check += denom[0] * denom[1]

  print("checksum:       {:10.2f}".format(check))
  print('\n')

### Main routine driver
if __name__ == "__main__":
  main()
