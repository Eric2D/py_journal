#The beginning

def main():
    import journal
    import passwords
    import shows
    import sys
    
    option1 = "Journal"
    option2 = "Passwords"
    option3 = "Shows"
    option4 = "Nevermind"

    user = raw_input("Your name, User?\n\n")
    if user == "Dying Flame": #Enter user name
        
    
        folder = raw_input("Hello User,\nShould I fetch your journal?\n\n    *Journal\n    *Passwords\n    *Shows\n    *Nevermind\n\n")

        if folder == option1:
            journal.inputs()
            main2()
        if folder == option2:
            passwords.inputs()
            main2()
        if folder == option3:
            shows.inputs()
            main2()
        if folder == option4:
            sys.exit()
        else:
            print("Sorry, I am not great at spontaneous conversation.\nPlease pick something from the list.\n\n")
            main2()
    else:
        sys.exit()
            
def main2():
    import journal
    import passwords
    import shows
    import sys
    
    option1 = "Journal"
    option2 = "Passwords"
    option3 = "Shows"
    option4 = "Nevermind"


    folder = raw_input("Anything else you would like to take care of User?\nWhat is on your mind?\n\n    *Journal\n    *Passwords\n    *Shows\n    *Nevermind\n\n")

    if folder == option1:
        journal.inputs()
        main2()
    if folder == option2:
        passwords.inputs()
        main2()
    if folder == option3:
        shows.inputs()
        main2()
    if folder == option4:
        sys.exit()
    else:
        print("Sorry, I am not great at spontaneous conversation.\nPlease pick something from the list.\n\n")
        main2()
    
