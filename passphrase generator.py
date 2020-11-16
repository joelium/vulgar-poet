#!/usr/bin/env python
# coding: utf-8

from random import choice, randint

# Function to add text file word list to python formatted list
def txt_to_list(file_name, split_char='\n'):
    """ Takes a text file input. By default the split between words it taken to be a newline character,
    but this can be changed by specifying the "split" value.
    
    Words are capitalised and added to a list variable that is then returned
    
    >>> variable = txt_to_list('word_list_1.txt')
    >>> variable = txt_to_list('word_list_1.txt', split=', ')
    """
    word_list = []
    
    # Open the word list file and split by the requested character
    for each in open(file_name).read().split(split_char):
        word_list.append(each.capitalize())
    open(file_name).close()
    
    # Return the list variable without last entry (empty)
    return word_list[:-1]


# Function to generate pass phrase

def gen_passphrase(length='', nums = True, sym = True):
    
    """Generate a passphrase from word lists. The passphrase can be randomly seeded with numbers
    and / or symbols to increase the security of the generated passphrase.
    
    >>> gen_passphrase()
    
    """
    try:
        if length == '':
            print('You must enter a length.')
            return
    except:
        print(length)
        return
    # Symbol list
    sym_list = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '+', '~', '-', '=', '#', '[', ']', 
                ';', ',', '.', '/', '{', '}', ':', '@', '<', '>', '?', '|', '\\']
    
    # Call above function to import word lists
    word_list_1 = txt_to_list('word_list_1.txt')
    word_list_2 = txt_to_list('word_list_2.txt')
    
    # Amount of total passphrase length for seed characters
    # 0.1 = 10%, 0.2 = 20%...
    seed_len = 0.2
    
    # Calculate maximum word length for each list
    max_wl_1 = max([len(x) for x in word_list_1])
    max_wl_2 = max([len(x) for x in word_list_2])
    
    # Calculate maximum passphrase length from word lists
    if nums or sym == True:
        max_len = round((max_wl_1 + max_wl_2) * (1 + seed_len))
    else:
        max_len = max_wl_1 + max_wl_2
    
    # Generate inital passphrase
        
    if length > max_len:
        print(f'Maximum phrase length is {max_len} characters')
        return
        
    elif length <10:
        print(f'Minimum phrase length is 10 characters')
        return
    
    else:
        fwl_1 = []
        fwl_2 = []
        
        for word in word_list_1:
            if nums or sym == True:
                tot_word_len = round(length * (1-seed_len))
                if ((tot_word_len / 2) - 1) < len(word) <= ((tot_word_len /2) + 1):
                    fwl_1.append(word)
            else:
                if (length / 2) - 1 < len(word) <= (length / 2) + 1:
                    fwl_1.append(word)
        cw = choice(fwl_1)
        
        for word in word_list_2:
            tot_word_len = round(length * (1-seed_len))
            if nums or sym == True:
                if ((tot_word_len / 2) - 1) < len(word) <= (tot_word_len /2):
                    fwl_2.append(word)
            else:
                if len(word) == length - len(cw):
                    fwl_2.append(word)
        passphrase = cw + choice(fwl_2)
        
    # This is the amount of spaces available to add seed characters to
    char_remain = length - len(passphrase)
    print(f'Preseed passphrase length: {len(passphrase)}')
    print(f'Preseed passphrase: {passphrase}')
    
    if nums or sym == True:
        split_word = []
        
        for letter in passphrase:
            split_word.append(letter)
            
        if nums and sym == True:
            print(f'Characters remaining: {char_remain}\nSymbols to be added: {round(char_remain/2)}')
            for i in range(round(char_remain/2)):
                split_word.insert(randint(0,len(passphrase)+1),choice(sym_list))
            for i in range(length - len(split_word)):
                split_word.insert(randint(0,len(passphrase)+1),choice([str(i) for i in range(0,10)]))
            print('Seed with symbols and numbers.')
            
        elif nums == True:
            for i in range(char_remain):
                split_word.insert(randint(0,len(passphrase)+1),choice([str(i) for i in range(0,10)]))
            print('Seed with numbers only.')
            
        else:
            for i in range(char_remain):
                split_word.insert(randint(0,len(passphrase)+1),choice(sym_list))
            print('Seed with symbols only')
            
        passphrase = "".join(split_word)
        #print(f'Final length: {len(split_word)}')
        
    else:
        print('No seed selected.')
        
    print(f'Requested passphrase length: {length}')
    print(f'Actual passphrase length: {len(passphrase)}')
    print(f'Final passphrase: {passphrase}')


print('Enter the desired passphrase length: ')
opt_len = int(input())
print('Include numbers? y/n (Default - yes): ')
opt_num = input()
print('Include symbols? y/n (Default - yes): ')
opt_sym = input()
gen_passphrase(length=opt_len, nums = opt_num, opt_sym = sym)
