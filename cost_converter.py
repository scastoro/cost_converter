codex = {
    "A": "0",
    "B": "1",
    "C": "2",
    "D": "3",
    "E": "4",
    "F": "5",
    "G": "6",
    "H": "7",
    "I": "8",
    "J": "9"
}

i = input('Type Here: ')

if ',' in i:
    x = i.split(',')
    totalCost = 0
    for code in x:
        cost = ""
        for letter in code:
            cost += codex[letter]
        totalCost += int(cost)
    print(totalCost)
else:
    cost = ""
    totalCost = 0
    for letter in i:
        cost += codex[letter]
    totalCost = int(cost)
    print(totalCost)
