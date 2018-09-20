#Passwords
def inputs():
    import io
    import os
    import source
    import glob
    import sys
    import edef

    pass_path = "pw\\"

    Password = raw_input("I have you password list.\n    *New entry\n    *Old entry\n    *Discard\n\n")

    if Password == "New entry":

    # os.linesep is being used to make a new line. Researching online someone had a similar problem and someone suggested using this, and it works.
    #The person's opinion was that the file is being opened in binary mode for some reason.

        passN = os.path.join(pass_path + raw_input("What is the account you are with?\n\n") + ".txt")
        with io.FileIO(passN, "a") as file:
            file.write(os.linesep + os.linesep + "Username: " + raw_input("The username?\n\n"))
            file.write(os.linesep + "E-mail: " + raw_input("The e-mail?\n\n"))
            file.write(os.linesep + "Password: " + raw_input("And finally, the password?\n\n") + os.linesep)
            file.close()

        print("you may ask me anytime for your memories.\n\n")
        return()

    if Password == "Old entry":
        password_files = glob.glob(pass_path + '*.txt')
        print edef.better_list(str(password_files), "\\", ".")
        rp = open(pass_path + raw_input("Which one do you want to remember?\n\n") + ".txt", "r")
        print rp.read()
        frp = raw_input("You can let me know when you are finished\n    *Finished\n\n")
        if frp == "Finished":
            rp.close()
        return()

    if Password == "Discard":
        password_files = glob.glob(pass_path + '*.txt')
        print edef.better_list(str(password_files), "\\", ".")
        forfile = pass_path + raw_input("Which would you like to delete?\n\n") + ".txt"
        os.remove(forfile)
        print("The memory has been deleted.")
        return()

    else:
        print("You will like the next update when I am an AI, we will have good conversations then, but if you would like to proceed, please pick one of the options\n\n")
        inputs()

