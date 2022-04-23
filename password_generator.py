# Password Generator - Hugo Oliveira

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+','-','_',' ','º',';','.','/','£','¢',';','¬','«','»','„','“','µ','•','·','.','º','~','´','ł','ĸ','ˀ','ħ','ŋ','đ','ð','ß','æ','ª','þ','ø','→','↓','←','ŧ','®','°','?']

print("SIMPLE PASSWORD GENERATOR")
nr_letters= int(input("How many letters would you like in your password?\n")) 
#nr_symbols = int(input(f"How many symbols would you like?\n"))
#nr_numbers = int(input(f"How many numbers would you like?\n"))

total_leters_0 = len(letters)
total_numbers_1 = len(numbers)
total_symbols_2 = len(symbols)
#summ_caracters = total_leters_ + total_numbers + total_symbols

password = ''

for carac in range(1,nr_letters+1):
  type_carac = random.randint(0,2)
  if type_carac == 0:
    letter_chosen = letters[random.randint(0,total_leters_0-1)]
    password += letter_chosen
  elif type_carac == 1:
    number_chosen = numbers[random.randint(0,total_numbers_1-1)]
    password += number_chosen
  else:
    symbol_chosen = symbols[random.randint(0,total_symbols_2-1)]
    password += symbol_chosen

print(password)
