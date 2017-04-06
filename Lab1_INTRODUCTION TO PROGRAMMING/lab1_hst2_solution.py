def is_isogram(argument):
  word_argument=set()
  if type(argument) != str:
    raise TypeError('Argument should be a string')
  if argument==" " :
    return(argument,False)
  argument.lower()
  argument = ''.join(argument.split())
  for letter in argument:
    if letter in word_argument:
      return(argument,False)
    word_argument.add(letter)
  return (argument,True)