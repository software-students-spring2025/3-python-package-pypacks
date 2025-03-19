#full text to slang words
from package.fullToSlang import fullToSlang
from package.slangToEmoji import slangToEmoji
from package.SlangToFull import SlangToFull

def full_to_slang(words):
    words = words.lower()
    for phrase, slang in fullToSlang.items():
        words = words.replace(phrase, slang)
    return words

import re

def slang_to_full(words):
    words = words.lower()
    for slang, phrase in SlangToFull.items():
        pattern = r'\b{}\b'.format(re.escape(slang))
        words = re.sub(pattern, phrase, words)
    return words


##slang to emojis
def slang_to_emoji(words):
    words = str(words).lower()
    for slang, emoji in slangToEmoji.items():
        words = words.replace(slang, emoji)
    return words

## remove slang words from a sentence
def remove_slang(words):
    words = words.lower()

    for slang in SlangToFull.keys():
        words = re.sub(r'\b{}\b'.format(re.escape(slang)), '', words)

    return " ".join(words.split())