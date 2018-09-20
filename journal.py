#Journal
def inputs():
    import io
    import os
    import source
    import glob
    import sys
    import edef

    thought_path = "jl\\"

    Journal = raw_input("I have fetched the journal.\n\n    *New entry\n    *Old entry\n    *Discard\n\n")


    if Journal == "New entry": 
        thoughtN = os.path.join(thought_path + raw_input("Shall we name this thought?\n\n") + ".txt")
        with io.FileIO(thoughtN, "a") as file:
            file.write(os.linesep + os.linesep + raw_input("When did this idea occur?\n\n"))
            file.write(os.linesep + raw_input("Well then, let's hear the story.\n\n") + os.linesep)
            file.close()

        print("Interesting, your thoughts will stay with me.\n\n")
        return()

    if Journal == "Old entry":
        thought_files = glob.glob(thought_path + '*.txt')
        print edef.better_list(str(thought_files), "\\", ".")
        rt = open(thought_path + raw_input("Which one do you want to remember?\n\n") + ".txt", "r")
        print rt.read()
        frt = raw_input("You can let me know when you are finished\n    *Finished\n\n")
        if frt == "Finished":
            rt.close()
        return()

    if Journal == "Discard":
        thought_files = glob.glob(thought_path + '*.txt')
        print edef.better_list(str(thought_files), "\\", ".")
        forfile = thought_path + raw_input("Which would you like to delete?\n\n") + ".txt"
        os.remove(forfile)
        print("The memory has been deleted.")
        return()

    else:
        print("Maybe if you chat with the creator he could give me more personality, but in the meantime, please choose one of the options.")
        inputs()
