#Vowel checker
from colorama import Fore 
import time 
import sys 
import random 
colors=(Fore.RED,Fore.YELLOW,Fore.GREEN,Fore.BLUE)
title='vowel checker\n'
for txt in title:
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write(f'\t{random.choice(colors)}{txt.upper()}')
else:
    while True:
     reset_to_default_color=Fore.RESET 
     print(f'{reset_to_default_color}')
     vowels=['a','i','e','o','u']
     letter=input('letter:')
     letter_length=1 
     if len(letter)>1:
         error_msg=f'Error, not {letter_length} character long'
         for txt in error_msg:
             time.sleep(0.1)
             print(f'{colors[0]}{txt}',end='')
         else:
             print(reset_to_default_color)
     else:
      if letter==vowels[0] or letter==vowels[1] or letter==vowels[2] or letter==vowels[3] or letter==vowels[4]:
        print('Your passed letter is a vowel')
      elif letter!=vowels[0] or letter!=vowels[1] or letter==vowels[2] or letter==vowels[3] or vowels[4]:
         print('Your passed letter is a consonant')