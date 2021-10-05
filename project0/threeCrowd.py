names = ["Aidan", "Dakin", "Nic", "Marvin"]

def crowdTest(names):
    if len(names) > 3:
        print("The room is too crowded")
crowdTest(names)
names.remove("Aidan")
names.remove("Nic")
crowdTest(names)