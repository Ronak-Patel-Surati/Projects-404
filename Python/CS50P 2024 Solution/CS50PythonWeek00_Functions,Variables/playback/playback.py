# Question : Playback Speed
# Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

# In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).








#take input
#use split maybe?
# add ... somehow?
#print, maybe with return ?/


#take input
controltheline = input("Give the me the for Playback control : ")

#starting googling why replace function is not working
line = controltheline.replace(" " , "...")
# did not have used controltheline.str.replace...  just use .replace


print(line)
