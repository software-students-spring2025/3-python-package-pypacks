from fullToSlang import fullToSlang

def full_to_slang(words: str) -> str:
    words = words.lower() 
    
    for phrase, slang in fullToSlang.items():
        words = words.replace(phrase, slang)
    return words
