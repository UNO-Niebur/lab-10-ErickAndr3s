#MapPlot.py
#Name: Erick Andres
#Date: 4/5/2026
#Assignment: Lab 10

import matplotlib.pyplot as plt
import csv

trials = []
reaction_times = []

with open("reaction_time_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        trial = int(row["Trial"])
        reaction_time = float(row["ReactionTime_ms"])


        if reaction_time > 0:
            trials.append(trial)
            reaction_times.append(reaction_time)

plt.plot(trials, reaction_times, marker='o')

plt.xlabel("Trial")
plt.ylabel("Reaction Time (ms)")
plt.title("Reaction Time vs Trial")

plt.savefig("reaction_time_graph.png")