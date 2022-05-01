phrase = input("Phrase to convert to acronym: ")

acronym_list = []

for space in range(phrase.count(" ") + 1):

    if phrase.__contains__(" "):
        thing = phrase[:phrase.find(" ") + 1]
        acronym = thing[:1]
        phrase = phrase[len(thing):]
    else:
        acronym = phrase[:1]
    acronym_list.append(acronym.upper())

print("".join(acronym_list))
