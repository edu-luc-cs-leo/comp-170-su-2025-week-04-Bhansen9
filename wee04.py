





def longest_word(words: list[str]) -> str:
    if words is not None and len(words) > 0:
        Word_Answer_LW = ""
        for word in words:
            if len(word) > len(Word_Answer_LW):
                Word_Answer_LW = word
        return Word_Answer_LW
    


def shortest_word(words: list[str]) -> str:
    Word_Answer_SW = None
    if words is not None and len(words) > 0:
        Word_Answer_SW = words[0]
        for word in words:
         if len(word) < len(Word_Answer_SW):
             Word_Answer_SW = word
    return Word_Answer_SW


def odd_words(words: list[str]) -> list[str]:
  list_of_odds = None
  if words is not None and len(words) > 0:
     list_of_odds = []
     for word in words:
        if (len(word) % 2 ) == 1:
          list_of_odds.append(word)
  return list_of_odds


def average_words(words: list[str]) -> list[str]:
  resulting_words = None
  if words is not None and len(words) > 0:
    resulting_words = []
    for word in words:
      avg_len = len(word) / len(words)
      difference = (len(word) - avg_len)
      if difference < 1:
        resulting_words.append(word)
  return resulting_words


def intersect(foo: list[str], bar: list[str]) -> bool:
  resulting_intersection = False
  if foo is not None and bar is not None and len(foo) > 0 and len(bar) > 0:
    for word in foo:
      if word in bar:
        resulting_intersection = True
  return resulting_intersection



"""  Looking at the solution and at my answer I can see some difference although my functions did do the job. 
I think the biggest take away is that I need to do a better job with type hints at the start of my function as I do not do it here in my function. 
The second thing is the labeling portions of my function. I think I'm definitely understanding the concepts in these homework assessments but I need to 
start including more time into the naming of my functions. I think my math part in the Diamond function was a little off as it does not include nearly as much as 
the solution does. I kind of came up with this formula on my own using the height of the Diamond as a key indicator on how the middle of the Diamond needs to be and 
going from there. I then was able to piece together the portions of the top and middle of both ends of the diamond using ratios and math that would compound on each other 
to assemble the symbols needed for each level. The right triangle I think I did a very good job on however I did not see that we had to do both sides facing left and right.
 The compound interest I feel as though I definitely got it. And the hollow square I feel like I got just not in the way that is shown in the solutions. Same as the diamond 
 I used my own formulas and just used the ratios to determine the amount of symbols and spaces needed for each level.   """












#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
