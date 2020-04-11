def break_words(stuff):
    print("This function break the stuff into words")
    words=stuff.split(' ')
    return words
    

def sort_words(words):
    print("This function sorts the word")
    return sorted(words) # this sorts words into list
    
    
def print_first_word(words):
    print("This function prints the first word")
    word= words.pop(0)
    return word
    
    
def print_last_word(words):
    print("This function returns the last word")
    word=words.pop(-1)
    return word
    
    
def sort_sentence(sentence):
    print("This function will return soted sentence")
    words=break_words(sentence)
    return sort_words(words)
    
    
def print_first_and_last(sentence):
    print("This function returns first and last word of the sentence")
    words=break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
def print_first_and_last_sorted(sentence):
    print("This function sorts the words and then print first and the last one")
    words=sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
    

   
    
    
    
    
    
    