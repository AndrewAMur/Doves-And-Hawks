import matplotlib.pyplot as plt
import numpy as np
import random

n = 0
m = 0

# This functions gets the top three birds from the table, and prints which bird there's more of.
# Hawks if there are more hawks, and Doves if there are more doves.

def criteria(table_of_birds):
    num_doves = 0
    num_hawks = 0
    top_birds = table_of_birds[0:3]

    for i in top_birds:
        if i[0] == "dove":
            num_doves += 1
        else:
            num_hawks += 1

    if num_doves > num_hawks:
        return "Doves are better"
    else:
        return "Hawks are better"

def simulation(n_dove, n_hawk, r, c):
    class Dove:
        def __init__(self):
            global n
            self.resource = 0
            self.type = 'dove'
            self.id = n
            n += 1

        def interaction(self, bird):
            if bird.type == 'hawk':
                self.resource += 0
            elif bird.type == 'dove':
                self.resource += r / 2


    class Hawk:
        def __init__(self):
            global m
            self.resource = 0
            self.type = 'hawk'
            self.id = m
            m += 1

        def interaction(self, bird):
            if bird.type == 'hawk':
                self.resource += r / 2 - c
            elif bird.type == 'dove':
                self.resource += r

    list_of_birds = []
    n_interactions = (n_dove + n_hawk) * 200

    for i in range(n_hawk):
        list_of_birds.append(Hawk())
    for i in range(n_dove):
        list_of_birds.append(Dove())

    for i in range(n_interactions):

        j = random.randint(0, len(list_of_birds) - 1)
        k = random.randint(0, len(list_of_birds) - 1)

        bird1 = list_of_birds[j]
        bird2 = list_of_birds[k]

        bird1.interaction(bird2)
        bird2.interaction(bird1)

    table = [(bird.type, bird.id, bird.resource) for bird in list_of_birds]

    table = sorted(table, key=lambda row: row[2], reverse=True)

    return table

def sum_birds(table):
    sum_doves = 0
    sum_hawks = 0


    for i in table:
        if i[0] == "hawk":
            sum_hawks += i[2]
        else:
            sum_doves += i[2]

    return sum_doves, sum_hawks

def resource_graphs(n_dove, n_hawk, resource):
    fight_cost_list = []
    resource_per_dove = []
    resource_per_hawk = []

    for fight_cost in range(0, 200, 20):
        table = simulation(n_dove, n_hawk, resource, fight_cost)
        resource_doves, resource_hawks = sum_birds(table)
        print(f"Doves: {resource_doves}, Hawks: {resource_hawks}, Fight Cost: {fight_cost}")
        fight_cost_list.append(fight_cost)
        resource_per_dove.append(resource_doves / n_dove)
        resource_per_hawk.append(resource_hawks / n_hawk)

    return fight_cost_list, resource_per_dove, resource_per_hawk

"""plt.plot(fight_cost_list, resource_per_dove, 'o', color='black', label="Doves")
plt.plot(fight_cost_list, resource_per_hawk, 'o', color='blue', label="Hawks")
plt.xlabel('Fight cost')
plt.ylabel('Sum of resources')
plt.legend()
plt.show()"""
# print(*table, sep="\n")
plt.figure(figsize=(12, 7))
plt.suptitle("Simulation Results")
n_dove_list = [25, 50, 75, 100]
n_hawk_list = [25, 50, 75, 100]
resource_list = [25, 50, 75, 100]
for subplot_number in range(1, 5):
    n_dove = n_dove_list[subplot_number - 1]
    n_hawk = n_hawk_list[subplot_number - 1]
    resource = resource_list[subplot_number - 1]

    fight_cost, y_dove, y_hawk = resource_graphs(n_dove, n_hawk, resource)
    plt.subplot(2, 2, subplot_number)
    plt.plot(fight_cost, y_hawk, color='red', label="Hawks")
    plt.plot(fight_cost, y_dove, color='blue', label="Doves")
    plt.title(f"n_doves: {n_dove}, n_hawks: {n_hawk}, resources: {resource}")
    plt.xlabel('Fight cost')
    plt.ylabel('Sum of resources')
    plt.legend()
    plt.grid()
plt.tight_layout()
plt.show()
