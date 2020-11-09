from tabulate import tabulate

li1 = ["Ronaldi", 23, 24, 40]
li2 = ["Messe", "22", "33", "43"]

print(tabulate(li1, li2, tablefmt="fancy_grid"))