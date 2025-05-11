#Welcome Message
print("Hey There! Welcome to your Personal Mood Journal!")

#Initializing Variables
moodJournal = {}
contMenu = True

#Essential Functions

#Display the main menu
def viewMenu():
    print("----------------")
    print("MAIN MENU")
    print("----------------")

    print("1. ✍🏻 Add Mood Journal Entry")
    print("2. 👀 View all Mood Data")
    print("3. 📒 View Single Day Entry")
    print("4. 📓 View Mood Summary")
    print("5. ❌ Exit")

#Get the action that the user wants to perform
def updateUserAction():
    try:
        return int(input("\nWhat would you like to do today?"))
    except ValueError:
        print("Oops! Invalid Input! Enter a value from 1 to 5!")
        return 0
    

#Adding a new mood journal entry    
def addNewEntry():
    print("Time to make a new mood entry!😊 ")
    print("\n")
    date = input("📅 Date (dd-mm-yyyy): ")
    mood = input("😊 Mood: ")
    note = input("📒 Note: ")

    #If no entry for the current date is found, add a blank entry
    if date not in moodJournal:
        moodJournal[date] = []
    
    #Make a new mood entry for the given date
    moodJournal[date].append((mood, note))

    #Confirmation Message
    print(f"Yaay! A new mood entry for the date {date} is added successfully!")

#View all the mood data for all the dates entered
def viewAllEntries():

    if not moodJournal:
        print("Your Mood Journal is empty! No entries found!")
    
    else:
        for date, entries in sorted(moodJournal.items()):
            print(f"\nDate: {date}")
            for mood, note in entries:
                print(f"{mood} - {note}")

def viewSingleDayEntry():
    userDate = input("Please enter the date to retrieve mood data(dd-mm-yyyy): ")

    if userDate in moodJournal:
        print(f"The mood entries for {userDate}")
        print("------------------------------------")
        for mood, note in moodJournal[userDate]:
            print(f"{mood} - {note}")

    else:
        print(f"Oops! No Entries found for the date {userDate}")

def viewMoodSummary():
    if not moodJournal:
        print("Your Mood Journal is empty! No entries found!")

    else:
        moodList = {}

        print("-------------")
        print("Mood Summary")
        print("-------------")

        #Loop through the mood journal to pick up all the listed moods
        for entries in moodJournal.values():
            for mood, note in entries:
                #Initialize count value for every new mood entry
                if mood not in moodList:
                    moodList[mood] = 0

                moodList[mood] += 1
        

        #Loop through the mood list and print out all the moods and their count
        for mood, count in moodList.items():
            print(f"{mood} - {count}")


# Keep the main program running until the user exits
while contMenu == True:

    viewMenu()
    userAction = updateUserAction()

    if userAction == 1:
        addNewEntry()
    
    elif userAction == 2:
        viewAllEntries()

    elif userAction == 3:
        viewSingleDayEntry()

    elif userAction == 4:
        viewMoodSummary()

    elif userAction == 5:
        print("Thanks for using our mood journal! See you later!")
        print("Exiting...")
        break

    cont = input("\nDo you want to continue? (y/n)").strip().lower()

    if cont != 'y':
        print("\nThanks for journaling with us! See you again!👋🏻")
        contMenu = False
    



