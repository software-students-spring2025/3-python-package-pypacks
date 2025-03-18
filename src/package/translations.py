#full text to slang words
from package.fullToSlang import fullToSlang
from package.slangToEmoji import slangToEmoji

def full_to_slang(words):
    words = words.lower()
    for phrase, slang in fullToSlang.items():
        words = words.replace(phrase, slang)
    return words

##slang to emojis
def slang_to_emoji(words):
    words = str(words).lower()
    for slang, emoji in slangToEmoji.items():
        words = words.replace(slang, emoji)
    return words