from fullToSlang import fullToSlang

def full_to_slang(words: str) -> str:
    words = words.lower() 
    
    for phrase, slang in fullToSlang.items():
        words = words.replace(phrase, slang)
    return words

if __name__ == "__main__":
    print(full_to_slang("Thank you for you help. I will talk to you later!"))