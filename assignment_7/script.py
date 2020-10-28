import matplotlib.pyplot as plt
import numpy as np


def parse_data(filename):
    ''' Parse the given file and return a list for males and list for females '''
    male = []
    female = []
    with open(filename, "rb") as file:
        lines = file.readlines()
        for line in lines:
            gender = line[474:475].decode('utf-8')
            weight = line[503:507].decode('utf-8')
            birth_day = line[22:23].decode('utf-8')

            if gender == "M":
                male.append({"weight": weight, "birth_day": birth_day})
            elif gender == "F":
                female.append({"weight": weight, "birth_day": birth_day})

    return male, female


def gender_proportion(x, y): return (len(x), len(y))


def gender_average_weight(x, y):
    ''' Returns average weight for males and females '''
    return (sum(int(i['weight']) for i in x)/len(x), sum(int(i['weight']) for i in y)/len(y))


def get_gender_births_weekday(x, y):
    ''' Returns amount of births on a weekday(0-6 indexed from Sun-Sat) for males and females '''
    male_days = []
    female_days = []
    for i in range(1, 8):
        male_days.append(
            len([day for day in x if int(day['birth_day']) == i]))
        female_days.append(
            len([day for day in y if int(day['birth_day']) == i]))

    return male_days, female_days


def plot_proporsion(list):
    xpos = np.arange(len(list))
    plt.figure(figsize=(12, 5))
    plt.bar(xpos-0.15, [i[0] for i in list], width=0.3, label="Male")
    plt.bar(xpos+0.15, [i[1] for i in list], width=0.3, label="Female")
    plt.title("Gender Proportion")
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.xticks(xpos, ("2017", "2018", "2019"))
    plt.savefig("proportion.png", dpi=500, bbox_inches="tight")


def plot_average_birth_weight(list):
    xpos = np.arange(len(list))
    plt.figure(figsize=(12, 5))
    plt.bar(xpos-0.15, [i[0] for i in list], width=0.3, label="Male")
    plt.bar(xpos+0.15, [i[1] for i in list], width=0.3, label="Female")
    plt.title("Average Birth Weight")
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.xticks(xpos, ("2017", "2018", "2019"))
    plt.savefig("avg_weight.png", dpi=500, bbox_inches="tight")


def plot_births_weekday(list):
    xpos = np.arange(7)
    plt.figure(figsize=(12, 5))
    plt.bar(xpos-0.25, [i for i in list[0][0]], width=0.1, label="Male 2017")
    plt.bar(xpos-0.15, [i for i in list[0][1]], width=0.1, label="Female 2017")
    plt.bar(xpos-0.05, [i for i in list[1][0]], width=0.1, label="Male 2018")
    plt.bar(xpos+0.05, [i for i in list[1][1]], width=0.1, label="Female 2018")
    plt.bar(xpos+0.15, [i for i in list[2][0]], width=0.1, label="Male 2019")
    plt.bar(xpos+0.25, [i for i in list[2][1]], width=0.1, label="Female 2019")
    plt.legend(bbox_to_anchor=(1.05, 1))
    plt.xticks(xpos, ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
    plt.savefig("birth_weekday.png", dpi=500, bbox_inches="tight")


proportion = []
avg_weight = []
births_weekday = []
files = ["2017.txt", "2018.txt", "2019.txt"]
for file in files:
    male, female = parse_data(file)
    proportion.append(gender_proportion(male, female))
    avg_weight.append(gender_average_weight(male, female))
    births_weekday.append(get_gender_births_weekday(male, female))

plot_proporsion(proportion)
plot_average_birth_weight(avg_weight)
plot_births_weekday(births_weekday)
