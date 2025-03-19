from translations import full_to_slang, slang_to_full, slang_to_emoji, remove_slang

def main():
    #example text for all the necessary conversions 

    text = "I love software engineering, omg , I don't know though I really need to stop procrastinating lol! #stem"

    print("Orginal Text:")
    print(text)


    #full text to slang 

    slang_text = full_to_slang(text)
    print("\nConverted to slang:")
    print(slang_text)

    #slang to full text 

    full_text = slang_to_full(text)
    print("\nConverted to full:")
    print(full_text)

    #slang to emojis 
    emoji_version =slang_to_emoji(text)
    print("\nConverted to emoji:")
    print(emoji_version)

    #removes slang
    remove_slang_from_text = remove_slang(text)
    print("\nRemoving all slang:")
    print(remove_slang_from_text)

if __name__ == "__main__":
    main()

