"""An adventure game where you play the role of an escaped prisioner!"""


from random import randint
player: str = ""
__author__ = "730414104"
points: int = 0
NAMED_CONSTANT: str = '\U0001F600'


def greet() -> None:
    """The greeting function!"""
    name: str = input("Whats your name sir? ")
    global player
    player = name
    print(f"{name}, you fool! I can't believe you were brazen enough to escape prison! You have no money, no food, and no armor. If you want to live, you're going to have to earn some money. There are gladiator pits up north, winning a some bouts up there should get you on your feet! Now scram! If the gaurds see me with your they will hang the both of us! ")


def main() -> None:
    """The actual game!"""
    print()
    greet()
    print()
    print("With your new found freedom, you can choose to either fight in the gladiator pit or hit the streets for supplies. Remember, The glatiators will scale to your strenght." + NAMED_CONSTANT + " ")
    i: int = 0
    print()
    while i < 3:
        decision: int = int(input("To roam the streets, enter 1. To fight in the pit, enter 2. To exit the game, enter any other number: "))
        if decision == 1:
            scavange(decision)
        elif decision == 2:
            strike: int = int(input("How many points do you want to wager? the more you wager, the more likely you are to win, but the more you will lose if you do lose!: "))
            global points
            points += fight(strike)
            print(points)
        else:
            i = 3
    print(f"Thanks for playing, you ended with {points} adventure points!")


def scavange(decision: int) -> None:
    """The player roams the streets!"""
    print("it gets dark and you meet some shady looking characters")
    counter = 0
    while counter < 4: 
        interaction = randint(1, 4)  
        print("you wonder down the alleys...")
        if interaction == 1:
            print(f"Hey, aren't you {player}, the dude who escaped prison? ")
            response_one: int = int(input("Enter 1 to lie or 2 to admit: "))
            if response_one == 1:
                charisma = randint(1, 2)
                if charisma == 1:
                    print("Yes you are! you're going to have to pay up for lying to us! ")
                    global points
                    points = points - 4
                else:
                    print("Oh my bad, sorry for bothering you! ")
            else:
                print("You're going to have to pay up to keep us quiet!")
                points = points - 2
        elif interaction == 2:
            print("You find some money on the ground!")
            points = points + randint(1, 3)
        elif interaction == 3:
            print("A man shouts: Stop, this is a robbery! give us your money!")
            response_three: int = int(input("Press 1 to surrender or 2 to fight back!: "))
            if response_three == 1:
                print("Yeah thats right you sucker!")
                points = 0
            else:
                struggle = randint(1, 5)
                if struggle == 5:
                    print("You got your butt kicked!")
                    points = 0
                else:
                    print("You easily throw the robber to the side")
                    points = points + 5
        elif interaction == 4:
            ("The night sky is beautiful")
            response_four: int = int(input("Enter 1 to appreciate the sky and 2 to ignore it: "))
            if response_four == 1:
                print("take the time to enjoy the little things")
                points = points + 1
            else:
                print("You should learn to appreciate the little things in life")
                points = points - 1
        counter = randint(1, 4)
    print("The night ends and a new day begins! ")
    print(points)


def fight(strike: int) -> int:
    """Fight in the gladiator pit!"""
    counterstrike: int = randint(1, points)
    if strike > counterstrike:
        print(f"Nice Job! you won against an opponent and earned {counterstrike} points")
        return counterstrike
    elif strike < counterstrike:
        print(f"You lost! you lost {strike} points :( ")
        return -1 * strike
    else:
        print("It's a draw! nothing happens :( ")
        return 0


if __name__ == "__main__":
    main()
