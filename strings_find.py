#The find() method is similar to index(), which you already know – it looks for a substring and returns the index of the first occurrence of this substring, but:

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))
#-----------------------------------------
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
#-----------------------------------------
#If you want to perform the find, not from the string's beginning, but from any position, you can use a two-parameter variant of the find() method. Look at the example:
print('kappa'.find('a', 2))
#-----------------------------------------
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)