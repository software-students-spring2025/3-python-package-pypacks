#full text to slang words
from package.fullToSlang import fullToSlang
def full_to_slang(words: str) -> str:
    words = words.lower()
    for phrase, slang in fullToSlang.items():
        words = words.replace(phrase, slang)
    return words

if __name__ == "__main__": 
    sentence = "I don't know. To be honest, this is a test" 
    print(f"Original: {sentence}")
    print(f"Slang:{full_to_slang(sentence)}")
