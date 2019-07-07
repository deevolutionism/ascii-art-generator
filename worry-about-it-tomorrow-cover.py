# generate album artwork
# roll the dice.
# 1-2 = "/"
# 3-4 = "\"
# 5-6 = "|"
# print out n number of characters

from random import choice

print( ''.join( choice( ['\\\\','/'] ) for i in range(1000) ) )