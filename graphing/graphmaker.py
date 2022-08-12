#!/usr/bin/env python3

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'chairs', 'tables', 'doors', 'couches', 'TVs', 'Computers' 
sizes = [9, 2, 2, 1, 1, 3]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # only "explode" all slices

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Things i can see from where im sitting.")
plt.savefig("/home/student/static/pie.png")
