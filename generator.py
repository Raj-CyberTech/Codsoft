# WELCOME NOTE BY THE CREATOR OF THIS PROJECT 


import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    while True:
        plen = int(input("\nENTER THE PASSWORD LENGTH :--- "))

        # Ensure password has at least one char from each group
        password = [
            random.choice(s1),
            random.choice(s2),
            random.choice(s3),
            random.choice(s4)
        ]

        # Fill the rest with random characters (repetition allowed)
        all_chars = s1 + s2 + s3 + s4
        password += random.choices(all_chars, k=plen - 4)

        # Shuffle to remove predictability
        random.shuffle(password)

        print("\n#### YOUR PASSWORD IS LISTED BELOW ::: ####")
        print("".join(password))

        # Ask user if they want another password
        again = input("\nDo you want to generate another password? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for using the Password Generator! 🔐")
            break
