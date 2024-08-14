from numpy import random

states = ["Bull", "Bear", "Stagnant"]
transitionName = [["AA", "AB", "AC"], ["BA", "BB", "BC"], ["CA", "CB", "CC"]]  # A = Bull, B = Bear and C = Stagnant
transitionMatrix = [[0.9, 0.075, 0.025], [0.15, 0.8, 0.05], [0.25, 0.25, 0.5]]


def market_trend(weeks):
    market_current = "Stagnant"
    print("Start state: " + market_current)
    market_sequence = [market_current]
    i = 0

    prob = 1
    while i != weeks:
        if market_current == "Bull":
            change = random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "AA":
                prob = prob * 0.9
                market_current = "Bull"
                market_sequence.append("Bull")
            elif change == "AB":
                prob = prob * 0.075
                market_current = "Bear"
                market_sequence.append("Bear")
            else:
                prob = prob * 0.025
                market_current = "Stagnant"
                market_sequence.append("Stagnant")
        elif market_current == "Bear":
            change = random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "BA":
                prob = prob * 0.15
                market_current = "Bull"
                market_sequence.append("Bull")
            elif change == "BB":
                prob = prob * 0.8
                market_current = "Bear"
                market_sequence.append("Bear")
            else:
                prob = prob * 0.05
                market_current = "Stagnant"
                market_sequence.append("Stagnant")
        elif market_current == "Stagnant":
            change = random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "CA":
                prob = prob * 0.25
                market_current = "Bull"
                market_sequence.append("Bull")
            elif change == "CB":
                prob = prob * 0.25
                market_current = "Bear"
                market_sequence.append("Bear")
            else:
                prob = prob * 0.5
                market_current = "Stagnant"
                market_sequence.append("Stagnant")
        i += 1

    print("Possible states: " + str(market_sequence))
    print("End state after " + str(weeks) + " weeks: " + market_current)
    print("Probability of the possible sequence of states: " + str(prob))
    return market_sequence


market_trend(2)

list_activity = []
count = 0

for iterations in range(1, 10000):
    list_activity.append(market_trend(2))

for smaller_list in list_activity:
    if smaller_list[2] == "Bear":
        count += 1

percentage = (count/10000) * 100
print("The probability of starting at state:'Stagnant' and ending at state:'Bear'= " + str(percentage) + "%")