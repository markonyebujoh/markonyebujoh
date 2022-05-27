# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    story = open(filename +".txt", "r")
    splits = story.read()
    
    
    return splits

read_file_content("story")

def count_words():
    text = read_file_content("story")
    
    brokenText = text.split()
    dictionary = dict()
    for word in brokenText:
        if word in dictionary.keys():
            dictionary[word] = dictionary[word]+1
        else:
            dictionary[word] = 1
    print(dictionary)
 


count_words()

