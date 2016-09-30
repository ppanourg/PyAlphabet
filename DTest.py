from DictionaryTrie import Dictionary, LoadDict

#dict = LoadDict.load()
dict = Dictionary()

"""Frequency orders of the below added elements:

   Starts with: D                       A              P         
                Don't vote for trump    Ammmurrica     Polynomial
                Dank                    Aardvark       Pandora's box
                Derp                    Abacus         Polly wanna cracker?
                                                                             """

print("\n\nPandora's box inserted?: " + str(dict.insert("Pandora's box", 1232)))
print("Derp inserted?: " + str(dict.insert("Derp", -5)))
print("Aardvark inserted?: " + str(dict.insert("Aardvark", 55)))
print("Dank inserted?: " + str(dict.insert("Dank", 123)))
print("Polynomial inserted?: " + str(dict.insert("Polynomial", 12333)))
print("Abacus inserted?: " + str(dict.insert("Abacus", 4)))
print("'Don't vote for trump' inserted?: " + str(dict.insert("Don't vote for Trump.", 9**5)))
print("'Polly wanna cracker?' inserted?: " + str(dict.insert("Polly wanna cracker?", 1231)))
print("Ammmurrica inserted?: " + str(dict.insert("Ammmurrica", 555)))

print("\n\nDerp reinserted?: " + str(dict.insert("Derp", -5)))
print("Aardvark reinserted?: " + str(dict.insert("Aardvark", 55)))
print("Dank reinserted?: " + str(dict.insert("Dank", 123)))
print("Abacus reinserted?: " + str(dict.insert("Abacus", 4)))
print("'Don't vote for trump' inserted?: " + str(dict.insert("Don't vote for Trump.", 9**5)))
print("Ammmurrica reinserted?: " + str(dict.insert("Ammmurrica", 555)))


print("\n\nPandora's box found?: " + str(dict.find("Pandora's box")))
print("Polynomial found: " + str(dict.find("Polynomial")))
print("'Polly wanna cracker?' found?: " + str(dict.find("Polly wanna cracker?")))
print("\n\nDerp found?: " + str(dict.find("Derp")))
print("Aardvark found: " + str(dict.find("Aardvark")))
print("Dank found?: " + str(dict.find("Dank")))
print("Abacus found?: " + str(dict.find("Abacus")))
print("'Don't vote for trump' found?: " + str(dict.find("Don't vote for Trump.")))
print("Ammmurrica found?: " + str(dict.find("Ammmurrica")))

print("\n\nderp found?: " + str(dict.find("derp")))
print("Ardvark found: " + str(dict.find("Ardvark")))
print("Dunk found?: " + str(dict.find("Dunk")))
print("Aabacus found?: " + str(dict.find("Aabacus")))
print("'Do vote for trump' found?: " + str(dict.find("Do vote for Trump.")))
print("Ammmurricas found?: " + str(dict.find("Ammmurricas")))

print("\n\nPredict top 100 for A: " + str(dict.predict("A", 100)))
print("\n\nPredict top 3 for D: " + str(dict.predict("D", 3)))
print("\n\nPredict top 5 for P: " + str(dict.predict("P", 10)))
print("\n\nPredict top 1 for A: " + str(dict.predict("A", 1)))
print("\n\nPredict top 0 for D: " + str(dict.predict("D", 0)))
print("\n\nPredict top 1 for P: " + str(dict.predict("Po", 1)))