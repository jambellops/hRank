'''

stringCapitalize

'''
# Complete the solve function below.
def solve(s):
    stringlist = list(s.split(' '))
    Printout = ' '.join(word.capitalize() for word in stringlist)
    return Printout
