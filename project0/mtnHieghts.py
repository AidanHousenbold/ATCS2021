mtns = {"Mount Everest": 8848, "Makalu": 8485, "Broad Peak": 8051, "Annapurna": 8091, "Cho Oyu": 8188}
print("Mountain Names:")
for mountain in mtns:
    print("  ", mountain)
print(" ")
print("Mountain Elevations:")
for mountain in mtns:
    print("  ", mtns[mountain])
print(" ")
print("Mountain:")
for mountain in mtns:
    print("  ", mountain, " is ",mtns[mountain], " meters tall")