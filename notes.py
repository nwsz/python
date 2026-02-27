from pypresence import Presence
import time

notes = []
print(f"Welcome to the notes app! You have {(len(notes))} notes.") # Introduces the user

# Sub-routines for options
def add():
    notes_add = input("What note do you want to add? ")
    notes.append(notes_add)
    for index, name in enumerate(notes):
        print(f"({index}) {name}")

def view():
    for index, name in enumerate(notes):
        print(f"({index}) {name}")
    if (len(notes)) == 0:
        print("You have no notes.")

def remove():
    type = input("Remove via index or name? ")
    if type == "name":
        note_remove = input("Enter the full name of the note to remove: ")
        notes.remove(note_remove)
        print(f"👍 Removed {note_remove}")
    elif type == "index":
        if len(notes) == 0:
            print("There are no notes to remove!")
        else:
            note_remove = int(input("Enter the index of the note to remove: "))
            note_remove -= 1

            if 0 <= note_remove < len(notes):
                removed_note = notes.pop(note_remove)
                print(f"👍 Removed '{removed_note}'")
            else:
                print("Woah, you can't remove that number, it doesn't exist!")

def purge():
    clear = 0
    totals = (len(notes))
    while clear != totals:
        notes.pop(0)
        clear = clear + 1
    for index, name in enumerate(notes):
        print(f"({index}) {name}")
    print("Finished clearing all!")


# Main Program for selector 
while True:
    selector = input("Would you like to add, view or remove notes? ")
    if selector == "add":
        add()
    elif selector == "view":
        view()
    elif selector == "remove":
        remove()
    elif selector == "purge":
        purge()
    else:
        print("You entered an incorrect option. Please try again")
