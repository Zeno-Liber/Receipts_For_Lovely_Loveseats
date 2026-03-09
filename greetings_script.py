print("Welcome to my Github! My name is Zeno (not my real name but privacy is important)")

user_name = input("What is your name friend? ")

greeting = "Well, nice to meet you, "

print(greeting + user_name + ". I hope you are having a pleasant day!")

user_choice = input(f"Which do you like more, dogs or cats, {user_name}? ")

upper_choice = user_choice.upper()

print(f"Take this on your adventure {user_name}!")

if upper_choice == "CATS" or upper_choice == "CAT":
    print(r"""
     /\_/\
    ( o.o )
     > ^ <
    """)
elif upper_choice == "DOGS" or upper_choice == "DOG":
    print(r"""
     / \__
    (    @\___
     /         O
    /   (_____/
    /_____/   U
    """)
else:
    print("Hey, that wasn't an option! You get nothing!")
