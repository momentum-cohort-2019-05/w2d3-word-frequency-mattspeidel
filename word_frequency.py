import re
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

dumped = open(file)
dumped = dumped.readlines()
dumped = ' '.join(dumped)
dumped = dumped.lower()
clean_dumped = re.sub(r'[^a-z ]', '', dumped)
clean_dumped = clean_dumped.split()
clean_dumped = sorted(clean_dumped)

word_list = []
for word in clean_dumped:
    if word in clean_dumped and word not in STOP_WORDS:
        word_list.append(word)

clean_list = {}
for word in word_list:
    if word in clean_list:
        clean_list[word] += 1
    else:
        clean_list[word] = 1

def printbynum(seq):
    return seq[1]

def print_formatted(formatted):
    formatted = sorted(formatted.items(), key=printbynum, reverse=True)
    for item, qty in formatted:
        print (f"{item}".rjust(16), " | "f"{qty}", "*" * qty)

print_formatted(clean_list)