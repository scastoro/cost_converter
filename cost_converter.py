
def cost_converter(codeInput):
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

    if ',' in codeInput:
        x = codeInput.split(',')
        totalCost = 0
        for code in x:
            cost = ""
            try:
                for letter in code:
                    if letter == ' ':
                        continue
                    else:
                        cost += codex[letter.upper()]
            except KeyError:
                return f"{letter} is incorrect"
            try:
                totalCost += int(cost)
            except:
                return "Something went wrong."
        return totalCost
    else:
        cost = ""
        totalCost = 0
        try:
            for letter in codeInput:
                if letter == ' ':
                    continue
                else:
                    cost += codex[letter.upper()]
        except KeyError:
            return f"{letter} is incorrect"
        totalCost = int(cost)
        return totalCost
