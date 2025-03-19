#full text to slang words
import string
from package.fullToSlang import fullToSlang
from package.slangToEmoji import slangToEmoji
from package.SlangToFull import SlangToFull

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def full_to_slang(words):
    words = words.lower()
    for phrase, slang in fullToSlang.items():
        pattern = r'\b{}\b'.format(re.escape(phrase))
        #words = words.replace(phrase, slang)
        words = re.sub(pattern, slang, words)
    
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
        pattern = r'\b{}\b'.format(re.escape(slang))
        #words = words.replace(slang, emoji)
        words = re.sub(pattern, emoji, words)
    return words






