
import random
import math

def objective(x):
    return (x - 3) ** 2


def simulated_annealing(initial, temp, cooling, min_temp, max_iter):

    current = initial
    current_cost = objective(current)

    best = current
    best_cost = current_cost

    for i in range(max_iter):

        if temp <= min_temp:
            break

        candidate = current + random.uniform(-1, 1)
        candidate_cost = objective(candidate)

        delta = candidate_cost - current_cost

        if delta < 0:
            accept = True
        else:
            probability = math.exp(-delta / temp)
            accept = random.random() < probability

        if accept:
            current = candidate
            current_cost = candidate_cost

        if current_cost < best_cost:
            best = current
            best_cost = current_cost

        temp = temp * cooling

    print("Best State:", round(best, 6))
    print("Minimum Function Value:", round(best_cost, 8))


# Input
initial = float(input("Enter initial state: "))
temp = float(input("Enter initial temperature: "))
cooling = float(input("Enter cooling rate: "))
min_temp = float(input("Enter minimum temperature: "))
max_iter = int(input("Enter maximum iterations: "))

seed = int(input("Enter random seed: "))
random.seed(seed)

simulated_annealing(initial, temp, cooling, min_temp, max_iter)
