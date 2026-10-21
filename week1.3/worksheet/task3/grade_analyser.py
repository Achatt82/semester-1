# Worksheet 1.3: Task 3

import csv

DEBUG = False
if DEBUG:
    import os

    # Hardcoded cwd for testing purposes
    os.chdir(r"E:\Dev\Python\semester-1\week1.3\worksheet\task3")

filename = input("Enter filename: ")

def CalculateGPA(grades):
    total, fq = 0, 0
    for grade in grades:
        total += grade
        fq += 1

    return total / fq

def CalculateDegree(gpa):
    degree = "0"
    match gpa:
        case _ if gpa >= 70:
            degree = "1"
        case _ if gpa >= 60:
            degree = "2:1"
        case _ if gpa >= 50:
            degree = "2:2"
        case _ if gpa >= 40:
            degree = "3"
        case _:
            degree = "F"

    return degree

with open(filename, "r", newline="") as file:

    out_filename = filename + "_out.csv"
    filename += ".csv"

    rdbuf = csv.reader(file)
    next(rdbuf)

    with open (out_filename, "w", newline="") as outfile:
        writer = csv.writer(outfile)

        for row in rdbuf:
            student_id = row[0]
            grades = row[1:]

            grades = [int(grade) for grade in grades if grade != ""]
            gpa = CalculateGPA(grades)
            degree = CalculateDegree(gpa)
            gpa = f"{gpa:.2f}"

            writer.writerow([student_id, gpa, degree])
