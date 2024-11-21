# Student Statistics Portal
# This program is a small example of how numpy can perform batch calculations on extensive data sets.
# Data from "grades.csv" is stored in a numpy array. Using numpy methods on the array and smaller slices give
# us insight on how well our students performed on each exam and across all exams.

import numpy as np

import re

# first function that starts the program, calls open_file()
def main():


    open_file()


# second function: it opens and reads the grades.csv file
def open_file():


    # open the grades file and refer to it as "file"
    with open("grades.csv", "r") as file:

        # assign all contents in file as "contents"
        contents = file.read()

        # split "contents" into a "grades_list"
        grades_list = re.split("\n|,", contents)

        # use list comprehension to divide the list into sub lists
        grades_list = [grades_list[i:i + 5] for i in range(0, len(grades_list), 5)]

    # convert the list into a numpy array and assign it to "a"
    a = np.array(grades_list)

    # call next function
    exam_stats_calculator(a)


# calculates statistics such as mean, median, standard deviation, minimum, and maximum
# of all_grades for each exam and across all exams
def exam_stats_calculator(a):


    # define specific slices from the array

    # numpy array of exam headers
    exam_headers = (a[0, 2:])

    # numpy array of all exam grades
    all_grades = (a[1:, 2:])

    # convert string values from numpy array into integers so
    # we can perform calculations on the data
    all_grades = all_grades.astype(int)

    # list of calculation headers
    calculation_headers = ["Average Grade", "Median Grade", "Standard Deviation", "Lowest Grade", "Highest Grade"]

    # accumulator that iterates through a column for each exam
    column_counter = 0

    # accumulator that serves as an index for referencing a nested list
    sublist_counter = 0

    # accumulator that serves as an index for referencing an item in a nested list
    item_counter = 0

    # holding place for formatting items and slicing, the slices get appended to exam_nums
    nums_sublist = []

    # accumulator for totalling up all students who passed
    total_passed = 0

    # accumulator for totalling up all exam grades regardless of passing or failing
    total_grades = 0

    # compares column_counter to the first row of "all_grades"
    # this ensures that all exams will be included
    while column_counter < len(all_grades[1]):

        # while using "counter" as a way to locate a singular column,
        # assign all data in current the column as "exam_grades"
        exam_grades = (all_grades[:, column_counter])

        # accumulating totals of how many students passed and failed this exam
        how_many_passed = 0
        how_many_failed = 0

        # tally up how many students passed and failed this exam
        for grade in exam_grades:

            if grade >= 60:

                how_many_passed += 1

            elif grade < 60:

                how_many_failed += 1


        # calculate the mean (average) grade for current exam
        mean = (np.mean(exam_grades))
        nums_sublist.append(mean)

        # calculate the median grade for current exam
        median = (np.median(exam_grades))
        nums_sublist.append(median)

        # calculate the standard deviation for current exam
        std = (np.std(exam_grades))
        nums_sublist.append(std)

        # calculate the minimum (lowest) grade for current exam
        min_ = (np.min(exam_grades))
        nums_sublist.append(min_)

        # calculate the maximum (highest) grade for current exam
        max_ = (np.max(exam_grades))
        nums_sublist.append(max_)

        # convert all the numbers in nums_sublist to integers 
        nums_sublist = [int(x) for x in nums_sublist]

        # append the new list of results to the exam_nums list by using list comprehension
        exam_nums = [nums_sublist[i:i+5] for i in range(0, len(nums_sublist), 5)]


        # statistics summary printed after all calculations for one exam
        print(f"-=-=-= {exam_headers[column_counter]} Statistics =-=-=-\n")

        # if-else statements that alter "students" to plural or singular based on
        # the number of how many passed and failed
        if how_many_passed == 1:

            print(f"{how_many_passed} student passed!")

        else:

            print(f"{how_many_passed} students passed!")

        if how_many_failed == 1:

            print(f"{how_many_failed} student failed.\n")

        else:

            print(f"{how_many_failed} students failed.\n")


        # add how_many_passed for this exam to "total_passed"
        total_passed += how_many_passed

        # add how_many_passed_ and how_many_failed to "total_grades"
        total_grades += how_many_passed + how_many_failed

        # "for" loop that iterates one time for each header in calculation_headers
        for header in calculation_headers:

            # print the data that goes with each calculation header
            print(f"{header}: {exam_nums[sublist_counter][item_counter]}% ")

            # add one to iterate through the items in the exam_nums nested list
            item_counter += 1

            # reset the item_counter to iterate through the next nested loop (next exam)
            if item_counter == len(calculation_headers):

                item_counter = 0
                print()

        # add one to the column counter to select the next exam
        column_counter += 1

        # add one to the sublist_counter to select the next nested list
        sublist_counter += 1


    # divide the total_passed(part) by total_grades(whole) to get an overall passing percentage and
    # format the result

    formt = '{:.3}'

    pass_percentage = formt.format(total_passed / total_grades * 100)

    # use numpy methods to calculate the overall class statistics

    # mean (average) grade of all grades
    mean = (np.mean(all_grades))

    # median grade of all grades
    median = (np.median(all_grades))

    # standard deviation of all grades
    std = (np.std(all_grades))

    # minimum (lowest) grade of all grades
    min_ = (np.min(all_grades))

    # maximum (highest) grade of all grades
    max_ = (np.max(all_grades))

    # gather the results into a list and convert them into integers
    overall_stats = [mean, median, std, min_, max_]
    overall_stats = [int(x) for x in overall_stats]

    # print the overall statistics starting with the pass percentage
    print("-=-=-= Overall Statistics =-=-=-\n")

    print(f"Pass percentage: {pass_percentage}%\n")

    # reset item_counter to 0
    item_counter = 0

    # iterates through each calculation header and prints the value corresponding to it
    # from the overall_stats list
    for header in calculation_headers:

        # the value of the item_counter is used to print the item at a specific index from overall_stats
        print(f"{header}: {overall_stats[item_counter]}%")

        # add one to the item_counter to print the next item in the overall_stats list
        item_counter += 1


# call first function
main()