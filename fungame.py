player_health = 100
player_shield = 100

while True:
    print("Health: " + str(player_health), ", Shield: " + str(player_shield))

    print("You are at the Village of Doom. You see before you three paths. Which path do you take?\n" +
          "1) The dark, dusty cave\n" +
          "2) The forbidden desert (DANGER AHEAD)\n" +
          "3) The enchanted forest\n")

    mageManor = input()
    if mageManor == "1":
        print("You are at the dark dusty cave")
    if mageManor == "2":
        print("You are in the forbidden desert")
    if mageManor == "3":
        print("Health: " + str(player_health), ", Shield: " + str(player_shield))
        print("You have entered the enchanted forest...\n Before you, you see " +
              "1) An evil graveyard, with a Frog waiting to be saved from the Mosquitos\n" +
              "2) Stay on same path\n" +
              "3) Contact Village and ask to leave\n")
    choiceCave = input()

    if choiceCave == "3":
            print("contact villager")
    elif choiceCave == "1":
            print("Health: " + str(player_health), ", Shield: " + str(player_shield))
            print(
                "You start to walk to the graveyard, but all of a sudden... EVIL monsters with their pet Mosquitos start to attack! What do you do?\n" +
                "1) Cast lightning bolt\n" +
                "2) Cast fireball\n" +
                "3) Heal\n")
            choice3 = input()
            if choice3 == "3":
                player_shield += 30
            elif choice3 == "2":
                player_shield -= 1
                print("You cast fireball... YOU SAVE THE FROG! You may continue down the path.")
            elif choice3 == "1":
                player_shield -= 45
                print(
                    "You cast lightning bolt. Rain starts to pour down! The zombies hurt you. You continue down the path.")

            print("Health: " + str(player_health), ", Shield: " + str(player_shield))
            break

print("THE CREEPER IS HERE!!!! WHAT DO YOU DO?\n" +
      "1) FIGHT!")

creeper_health = 250

while True:
    if input():
        print("Health: " + str(player_health) + ", Shield: " + str(player_shield) + ", Creeper Health: " + str(
            creeper_health))
        print(
            "What do you do?\n" +
            "1) Cast lightning bolt\n" +
            "2) Cast fireball\n" +
            "3) Heal\n")
        choice3 = input()
        if choice3 == "3":
            player_shield += 30
        elif choice3 == "2":
            player_shield -= 50
            player_shield -= 5 * 10
            creeper_health -= 100
            print("You cast fireball... You lost 100 Shield! The creeper lost 100 health!")
        elif choice3 == "1":
            player_shield -= 25
            creeper_health -= 50
            print("You cast lightning bolt. The creeper kind of hurts. You lost 25 shield!")

        if creeper_health <= 0:
            while True:
                print("Health: " + str(player_health) + ", Shield: " + str(player_shield))
                print("The creeper ignites and exploded! The mini creepers attack!\n" +
                      "What do you do?\n" +
                      "1) Cast lightning bolt\n" +
                      "2) Cast fireball\n" +
                      "3) Heal\n")
                choice4 = input()
                if choice4 == "1" or choice4 == "2":
                    player_shield += 50
                    print("You defeated the creeper and its mini minions! Congratulations!\n You head towards the mansion.\n" +
                          "You find a maze, inside the mansion. What do you do?\n" +
                          "1) Go left\n" +
                          "2) Go straight\n" +
                          "3) Go right")
                    if input() == "1":
                        print("Theres an AMBUSH! You die. Sorry! You have a nice funeral at the village of Doom. You should have listened to Mom.")
                        break
                    elif input() == "3":
                        print("You die to a pitfall trap filled with zombies. Your body is never found. You should have listened to Mom.")
                        break
                    elif input() == "2":
                        print("You found the treasure! Thank God you listened to your mom! The end........")
                        break
                if choice4 == "3":
                    player_health += 30
                    print("You healed! +30 Health!")