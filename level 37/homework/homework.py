#1
def array(string):
    list1 = string.split(',')
    if len(list1) <= 2:
        return None
    else:
        return ' '.join(list1[1:-1])
#2
def contamination(text, char):
  return "".join(char for x in text)
#3
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]