import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regex to find "um" as a standalone word, case-insensitively
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()
