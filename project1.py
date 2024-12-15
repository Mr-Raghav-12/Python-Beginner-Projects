# This is a beginner-level guide to making Python projects that beginners can try. This Is Project 1
# Created by @hqbeast on Telegram and @Mr-Raghav-12 on GitHub Both Are My Own Accounts

import time
import random

def random_num():
    return random.randint(100, 99999)

# Get user input
first = input("Enter your first name: ")
last = input("Enter your last name: ")

# Greet the user and explains about the project.
print(f"\nHello \"{first} {last}\"! This is a beginner-level project. Let's see what random username you get!")
time.sleep(2)
#It Generate a new username using the random_num function. Display a random username by combining the first name, a random number, and the last name, separated by an underscore (_),you can directly add (_) but i used sep because clearing that topic.
print(f"\"{first}\", your username will be:", end=" ")
print(f"{first}{random_num()}{last}",sep="_")
