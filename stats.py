
import string
import sys


def get_book_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read().lower()
        return file_contents
    
def get_word_count(file_contents):
    word_split= file_contents.split()
    word_count = len(word_split)
    return word_count

def get_character_count(file_contents):
    char_count = {}
    for char in file_contents:
        char_count[char] = char_count.get(char,0)+1
    return char_count


def sort_on(items):
    return items["num"]

def get_sorted_character_coutn(file_contents):
    char_count = {}
    for char in file_contents:
        if char.isalpha():
            char_count[char] = char_count.get(char,0)+1
    char_list = []
    for char,count in char_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    
    char_list.sort(reverse=True, key = sort_on)


    return char_list
 
                      
        