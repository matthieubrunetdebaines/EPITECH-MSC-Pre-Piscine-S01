# quit_the_shire = ["monday", "3:30 PM", "Frodo", "Sam", "Merry", "Pippin"]
# rivendel = ["wednesday", "5:00 PM", "Frodo", "Sam", "Merry", "Pippin", "Gandalf", "Aragorn"]
# helm= ["friday", "9:00 PM", "Gandalf", "Aragorn"]
# minas_tirith= ["saturday", "5:00 AM", "Gandalf", "Pippin"]
fellowship_member=input("Which member of the fellowship are you?")

an_adventure= [
    {
    "meeting_name": "Quit_the_shire",
    "day":"monday",
    "time":"3:30 PM",
    "members":["Frodo", "Sam", "Merry", "Pippin"]
    },
    {
    "meeting_name": "Rivendel",
    "day":"wednesday",
    "time":"5:00 PM",
    "members":["Frodo", "Sam", "Merry", "Pippin", "Gandalf"]
    },
    {
    "meeting_name": "Helm",
    "day":"friday",
    "time":"9:00 PM",
    "members":["Gandalf", "Aragorn"]
    },
    {
    "meeting_name": "Minas_tirith",
    "day":"saturday",
    "time":"5:00 AM",
    "members":["Pippin", "Gandalf"]
    },
]

for meeting in an_adventure:
    if fellowship_member in meeting["members"]:
        print(f"You are planned on: {meeting['meeting_name']} on {meeting['day']} at {meeting['time']}")
    # else:
    #     print("No adventure, you fool!")