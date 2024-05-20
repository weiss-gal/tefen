"""
This code "encrypts" a string by replacing the letters in a constant pattern.
"""



def scramble(s: str, offset: int) -> str:
    new_s = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                new_s += chr((ord(c) - ord('a') + offset) % 26 + ord('a'))
            else:
                new_s += chr((ord(c) - ord('A') + offset) % 26 + ord('A'))
        else:
            new_s += c

    return new_s


def unscramble(s: str) -> str:
    pass

def main():
    s = """
    Well done, 
    you have successfully solved the riddle, 
    this secret message is encrypted using a simple method that is sometimes called a "Caesar cipher."
    To get your price, the secret word you should know is "Avocado."
    
    """

    s2 = scramble(s, 7)
    print(s2)
    s3 = unscramble(s2)
    print(s3)

if __name__ == "__main__":
    main()