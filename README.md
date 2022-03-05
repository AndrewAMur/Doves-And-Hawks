# Doves-And-Hawks
## Introduction
The hawk-dove model is an evolutionary game theoretical model developed by John Maynard Smith (1982) depicting the fundamental conflict between prosocial (altruism and cooperation) and antisocial behavior (selfishness). The model describes the contest between two fundamentally different behavioral strategies, hawks (selfishness) and doves (pro-sociality), when competing over a shared resource. 
V – amount of resources
C – Fight cost
![Screenshot](Pictures/diagram.jpg.png)
This contest reveals the evolutionary paradox of prosocial behavior (i.e., if natural selection is based on competition, then prosocial traits should not evolve). The hawk-dove model provides a simplistic framework to investigate the conditions that favor the evolution of prosocial behavior. 
Overall, hawks outcompete doves within groups, but a group of doves outcompete a group of hawks. For either hawks or doves to evolve, the balance of selection within and between groups must tip in their respective favor. 
I used this evolutionary model in my project to see what species of birds had a better chance of survival. I had thought that the Hawks were the more supreme species because they keep all of the recourses to themselves, but as it turns out, the Doves had many more times as many recourses than the Hawks, making their evolutionary model the best for all species.
## Simulation
I wrote a program using the Python programming language to simulate the interaction of Doves and Hawks. The program implements random interactions between the two classes of birds. Every instance of the class has an attribute to store its resource amount from all previous interactions. Every simulation initializes the number of birds in each species and runs a given number of interactions after which, it returns the table.
The criteria for the table was to choose the top 3 birds with the highest resource amount. If there are more doves than hawks, the doves win, and if there are more hawks than doves, the hawks win.
## Results
At the end of the program, we made for loop to give many values for the fight cost.
