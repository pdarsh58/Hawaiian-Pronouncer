#Hawaiian Pronouncer
#Darshil Patel

def validHawaiianword():
    
    valid = True   
    while valid:
        word = input("Enter a hawaiian word to pronounce: ")

        countletters = 0
        for letter in word:
            if letter in "aeioupkhlmnw' ":
                countletters += 1
                valid = False
                
        if countletters == len(word):
            valid = False
        else:
            valid = True
        
    return str(word)


        
def hawaiian_pronuncer():
    word = str(validHawaiianword())
    word = word.lower()
    
    if "iw" in word or "ew" in word:
        word = word.replace('w', 'v')
    if "uw" in word or "ow" in word:
        word = word.replace('w', 'w')

    grpVowels = {'ai':'eye-', 'ae':'eye-', 'ao':'ow-', 'au':'ow-','ua':'oo-ah-','ei':'ay-', 'eu':'eh-oo-','iu':'ew-','oi':'oyo-','ou':'ow-','ui':'ooey-'}
    vowels = {'a':'ah-', 'e':'eh-', 'i':'ee-', 'o':'oh-', 'u':'oo-'}    
    
    new_word = ""    

    for index in range(len(word)):

        #for consonants
        if word[index] in "pkhlmnvw' ":
            new_word += word[index]
        
        #for vowels
        if word[index] in "aeiou":

            #for grouped vowels:
            if (index + 1) < len(word) and (word[index + 1] in "aeiou"):
                
                grp = str(word[index]) + str(word[index + 1])
                if grp in grpVowels:
                    new_word += grpVowels[grp]
                else:
                    for char in grp:
                        new_word += vowels[char]
              
            #for single vowels             
            if (word[index - 1] not in "aeiou") and (word[index] in "aeiou"):
                if ((index + 1) < len(word)) and (word[index + 1] not in "aeiou"):
                    new_word += vowels[word[index]]
                
            #for last letter
            if (index == (len(word) - 1)) and (word[index - 1] not in "aeiou"):
                if word[index] in "pkhlmnvw'":
                    new_word += word[index]
                if word[index] in "aeiou":
                    new_word += vowels[word[index]]

            #for first letter
            if index == 0 and (word[index] in "aeiou"):
                new_word += vowels[word[index]]     
                               
    new_word = new_word.capitalize()
    """if new_word[-1] == "-":
        new_word = new_word[:-1]
    """
    return new_word       

print(hawaiian_pronuncer())

    
