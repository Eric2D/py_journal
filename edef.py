#This definition takes in a string and searches from one point to another
#and prints out the items in seperate lines making a clean list.
#only works if there is a breaking point between words in the string

def better_list(l, fro, to):
    phrase_beg = l.find(fro) + 1
    phrase_end = l.find(to)
    entry_num = 0
    while phrase_beg != 0:
        print l[phrase_beg:phrase_end]
        phrase_beg = l.find(fro, phrase_beg + 1) + 1
        phrase_end = l.find(to, phrase_end + 1)
        entry_num = entry_num + 1
    return str(entry_num) + " entries"

