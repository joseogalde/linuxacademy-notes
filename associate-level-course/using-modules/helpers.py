#__all__ = ['extract_lower'] #setting this variable gives you control about the methods that you want to export when somebody does a from helpers import * 

#if we set the name of this function to start with underscore, it will be hided for importing purposes.
def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

#def extract_upper(phrase):
#    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))

if __name__ == "__main__":
    print("HELLO FROM HELPERS")

    print(f"__name__ in helpers.py: {__name__}")
