def isValid(test_str):
  # len(test_str) is odd -> invalid!
  if len(test_str)%2 != 0:
    return False
  # initialize parentheses dict
  par_dict = {'(':')','{':'}','[':']'}
  stack = []
  for char in test_str:
    # push opening bracket to stack
    if char in par_dict.keys():
      stack.append(char)
    else:
      # closing bracket without matching opening bracket
      if stack == []:
          return False
      # if closing bracket -> pop stack top
      open_brac = stack.pop()
      # not matching bracket -> invalid!
      if char != par_dict[open_brac]:
        return False
  return stack == []

print(isValid('()]'))