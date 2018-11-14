'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .
For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Input Format
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A - Z].

Constraints


Output Format
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.
'''

def minion_game(string):
    # your code goes here

    Vowels = ('A', 'E', 'I', 'O', 'U')
    ConsonantPlayer = 'Stuart'
    ConsonantScore = 0
    VowelPlayer = 'Kevin'
    VowelScore = 0
    sLen = len(string)
    for i in range(sLen):
        if string[i] in Vowels:
            VowelScore += sLen - i
        else:
            ConsonantScore += sLen - i

    if ConsonantScore > VowelScore:
        print(ConsonantPlayer, ConsonantScore)
    elif ConsonantScore == VowelScore:
        print('Draw')
    else:
        print(VowelPlayer, VowelScore)
