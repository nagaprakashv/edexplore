
# Generic patterns
NUM_REGEX = r"^\d+$|^\d+\.\d+$|^\d+\.\d\d$"
STR_REGEX = r"\D+[\s|\D]\D+|\D+"
# ALPHANUM_REGEX = 

# Spacing patterns
WHITESPACE = r"\s\s+"
LEADINGTRAILING = r"^\s|\s$"
SPACINGISSUES = r"[a-z][A-Z]|\d+[a-zA-Z]{3}|[a-zA-Z]+\d+"

# Formatting patterns
HTMLTAGS = r"\<[^>]*\>?"
UNICODEWEIRD = r"\\[a-zA-Z1-9]{3,4}|[^\x1F-\x7F]+"

# Additional patterns
ISNOTNULL = r""

# Ordered dictionary
REGEX_DICT = {"is string":STR_REGEX,
              "is numeric":NUM_REGEX,
              "is not null":ISNOTNULL,
              "extra spaces": WHITESPACE,
              "lead./trail. spaces": LEADINGTRAILING,
              "missing spaces": SPACINGISSUES,
              "html tags": HTMLTAGS,
              "unicode char.": UNICODEWEIRD}