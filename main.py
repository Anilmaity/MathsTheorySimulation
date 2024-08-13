import random
import matplotlib.pyplot as plt


total_capital = 1000
min_capital = 100

# Parameters
number_of_trades = 100
targets = [(50, 0.5)]
stoploss = [(-41, 0.5)]

# Extract probabilities and outcomes
target_values, target_probs = zip(*targets)
stoploss_values, stoploss_probs = zip(*stoploss)

# Combine targets and stoplosses for easier handling
outcomes = target_values + stoploss_values
probs = target_probs + stoploss_probs

# Normalize probabilities (if needed)
total_prob = sum(probs)
if total_prob < 1.0:
    outcomes += (0,)
    probs += (1.0 - total_prob,)

# Simulate trades
results = []
cumulative_results = []
total_result = 0
for _ in range(number_of_trades):
    outcome = random.choices(outcomes, probs)[0]
    results.append(outcome)
    total_result += outcome
    cumulative_results.append(total_result)

# Plot the results
# plt.figure(figsize=(10, 6))
# plt.plot(cumulative_results, label='Cumulative Profit/Loss')
# plt.xlabel('Trade Number')
# plt.ylabel('Cumulative Profit/Loss')
# plt.title('Trading Simulation Results')
# plt.legend()
# plt.grid(True)
# plt.show()

# Calculate total profit/loss
total_result = sum(results)
# print(f"Outcomes: {results}")
print(f"Total result after {number_of_trades} trades: {total_result*25}")


# Keely Criteria

# b = x/y # x = profit, y = loss
# constant wager

#fixed percentage = P(H) - (P(L)/b)

