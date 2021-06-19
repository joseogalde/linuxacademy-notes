from helpers.strings import extract_lower, extract_upper
from helpers import variables
import helpers

print(f"Lowercase letters: {extract_lower(variables.name)}")
print(f"Uppercase letters: {extract_upper(variables.name)}")
print(f"From helpers: {helpers.strings.extract_lower(variables.name)}")
