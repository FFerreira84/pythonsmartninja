#!/usr/bin/env python
# -*- coding: utf-8 -*-

# guest = 0
# secret = 7
#
# while guest != secret:
#     guess = int(raw_input("Guess the secret number: "))
#     if secret == guess:
#         print "You guessed correctly!"
#         break
#     else:
#         print "You guessed wrong!"


# secret = 7
# guess = 0
#
# for x in range(5):
#     guess = int(raw_input("Guess the secret number: "))
#     if secret == guess:
#         print "You guessed correctly!"
#     elif x < 3:
#         print "You guessed wrong! You have " + str(4-x) + " guesses left."
#         if guess > secret:
#             print "Try a lower number."
#         else:
#             print "Try a higher number."
#     elif x == 3:
#         print "You guessed wrong! You have 1 guess left."
#         if guess > secret:
#             print "Try a lower number."
#         else:
#             print "Try a higher number."
#     elif x > 3:
#         print "You guessed wrong! Game over!"



# secret = 7
# guess = 0
# x = 5
#
# while x > 0:
#     x -= 1
#     guess = int(raw_input("Guess the secret number: "))
#     if secret == guess:
#         print "You guessed correctly!"
#         break
#     elif x > 1:
#         print "You guessed wrong! You have " + str(x) + " guesses left."
#         if guess > secret:
#             print "Try a lower number."
#         else:
#             print "Try a higher number."
#     elif x == 1:
#         print "You guessed wrong! You have 1 guess left."
#         if guess > secret:
#             print "Try a lower number."
#         else:
#             print "Try a higher number."
#     elif x == 0:
#         print "You guessed wrong! Game over!"


# opcao = "S"
# while opcao == "S":
#     km = int(raw_input("Este programa converte quilómetros para milhas. Por favor insira o valor em quilómetros: "))
#     print "O valor que inseriu corresponde a " + str(km*0.621371192) + " milhas."
#     opcao = raw_input("Pretende fazer uma nova conversão? (S/N): ")


# num = int(raw_input("Selecione um número entre 1 e 100: "))
#
# for i in range(1, num+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print "fizzbuzz"
#     elif i % 3 == 0:
#         print "fizz"
#     elif i % 5 == 0:
#         print "buzz"
#     else:
#         print i

opcao = "S"
while opcao == "S":
    frase = raw_input("Este programa converte uma string para letras minúsculas. Insira a sua string: ")
    print (frase.lower())
    opcao = raw_input("Pretende fazer uma nova conversão? (S/N): ")

