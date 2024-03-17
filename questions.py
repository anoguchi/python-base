#!/usr/bin/env python3

def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter.")

def ask_question(ask_color=False):
    name = input("name: ")
    print(f"It is nice to meet you {name}")

    if ask_color:
        color = input("What is your favorite color? ")
        print(f"{color} is a great color!")

    input("Describe yourself: ")
    print("Very nice 😉")

def goodbye():
    print("Goodbye.")

welcome()
ask_question(ask_color=True)
goodbye()
