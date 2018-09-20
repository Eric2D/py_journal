# Input Script Module

thought_path = "jl\\"
pass_path = "pw\\"

def new_entry():
    import io
    import os
    import source
    something_new = raw_input("Is that so? What are your thoughts?\n    *Journal\n    *Passwords\n\n")

    if something_new == "Journal":
        
        thoughtN = os.path.join(thought_path + raw_input("Shall we name this thought?\n\n") + ".txt")
        with io.FileIO(thoughtN, "a") as file:
            file.write(os.linesep + os.linesep + raw_input("When did this idea occur?\n\n"))
            file.write(os.linesep + raw_input("Well then, let's hear the story.\n\n") + os.linesep)
            file.close()

        print("Interesting, your thoughts will stay with me.\n\n")
        return()       

        
    if something_new == "Passwords":

    # os.linesep is being used to make a new line. Researching online someone had a similar problem and someone suggested using this, and it works.
    #The person's opinion was that the file is being opened in binary mode for some reason.

        
        passN = os.path.join(pass_path + raw_input("What is the account you are with?\n\n") + ".txt")
        with io.FileIO(passN, "a") as file:
            file.write(os.linesep + os.linesep + "Username:" + raw_input("The username?\n\n"))
            file.write(os.linesep + "E-mail:" + raw_input("The e-mail?\n\n"))
            file.write(os.linesep + "Password:" + raw_input("And finally, the password?\n\n") + os.linesep)
            file.close()

        print("you may ask me anytime for your memories.\n\n")
        return()
    else:
        print("I wish we could have more spontaneous conversation, but please choose one of the options.")
        new_entry()
        
def remembering():

    import os
    import glob
    import source

    remembered = raw_input("Of course User. I never forget, unless you ask me to of course.\n    Journal?\n  Or\n    Passwords?\n\n")
    
    if remembered == "Journal":
        thought_files = glob.glob(thought_path + '*.txt')
        print (thought_files)
        rt = open(thought_path + raw_input("Which one do you want to remember?\n\n") + ".txt", "r")
        print rt.read()
        frt = raw_input("You can let me know when you are finished\n    *Finished\n\n")
        if frt == "Finished":
            rt.close()
        return()
        
    if remembered == "Passwords":
        password_files = glob.glob(pass_path + '*.txt')
        print(password_files)
        rp = open(pass_path + raw_input("Which one do you want to remember?\n\n") + ".txt", "r")
        print rp.read()
        frp = raw_input("You can let me know when you are finished\n    *Finished\n\n")
        if frp == "Finished":
            rp.close()
        return()    
    else:
        print("Maybe if you chat with the creator he could give me more personality, but in the meantime, please choose one of the options.")
        remembering()
            
def forgetting():
    
    import source
    import os
    import glob
        
    forgetting = raw_input("Understand that there is no getting the information back User.\nWhat would you like to delete?\n    *Journal\n    *Passwords\n\n")

    if forgetting == "Journal":
        thought_files = glob.glob(thought_path + '*.txt')
        print(thought_files)
        forfile = thought_path + raw_input("Which would you like to delete?\n\n") + ".txt"
        os.remove(forfile)
        print("The memory has been deleted.")
        return()
                
    if forgetting == "Passwords":
        password_files = glob.glob(pass_path + '*.txt')
        print(password_files)
        forfile = pass_path + raw_input("Which would you like to delete?\n\n") + ".txt"
        os.remove(forfile)
        print("The memory has been deleted.")
        return()
    else:
        print("You will like the next update when I am an AI, we will have good conversations then, but if you would like to proceed, please pick one of the options")
        forgetting()


#FINISHED
def mind_changer():
    import sys
    
    bye = raw_input("I suppose I will see you later User.\nHave a nice rest of your day.\n\n")
    if bye == "See you later":
        sys.exit()
    else:
        sys.exit
