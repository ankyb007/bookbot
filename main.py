from stats import num_of_words
from stats import num_of_chars
from stats import sorted_dict
import sys

if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path=sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents


def main():
    #book_path="books/frankenstein.txt"
    content=get_book_text(book_path)
    num_words=num_of_words(content)
    counted= num_of_chars(content)
    lst=sorted_dict(counted)
    print("\n=========BOOKBOT=============\n")
    print(f"Analyzing book found at {book_path}...\n")
    print("---------Word Count ---------")
    print(f"Found {num_words} total words\n")
    print("---------Character Count-----")
    
    for i in lst:
        print(f"{i["name"]}: {i["num"]}")

    print("\n")

#    lst=[]
#    for i in counted:
#        exmp={}
#        exmp["name"]=i
#        exmp["num"]=counted[i]
#        lst.append(exmp)

#    print(lst)

main()
