#full text to slang words
from package.fullToSlang import fullToSlang
def full_to_slang(words):
    words = words.lower()
    for phrase, slang in fullToSlang.items():
        words = words.replace(phrase, slang)
    return words

#this is just to check if my function words (Ajok)
if __name__ == "__main__": 
    sentence = "I don't know. To be honest, this is a test" 
    print(f"Original: {sentence}")
    print(f"Slang:{full_to_slang(sentence)}")