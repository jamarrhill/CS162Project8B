# Name: Jamar Hill
# Date: 5/24/2021
# Description: CS 162 Project 8B

import random
import time
import matplotlib.pyplot as pyplot

def bubble_sort(values):
    for i in range(len(values)-1):
        for j in range(len(values)-i-1):
            if (values[j] > values[j+1]):
                var = values[j]
                values [j] =values [j+1]
                values[j+1] =var

def insertion_sort(values):
    for i in range(1, len(values)):
        var =values[i]
        j = i-1
        while (j >=0 and var< values[j]):
            values[j+1]=values[j]
            j = j-1
        values[j+1] = var

def sort_timer(function): #Initiate decorator method of timing sort
    def sort_decorator(numbers): #Decorator Method
        begin_time=time.perf_counter() #Vairable begin_time initiates time module
        function(numbers)
        end_time=time.perf_counter() #variable end_time stops the timer
        return end_time-begin_time #Calculates the final run time
    return sort_decorator

def compare_sorts(decoratorA_bubble, decoratorB_insertion): #comparing both sort methods
    x_values=[] #Create list for x values
    y_values_decoratorA=[] #y values for bubble_sort
    y_values_decoratorB =[] #y values for insertion_sort

    for size in range(1000,10001,1000): #for loop in range 1000-10000 in 1000 steps

        values =[random.randint(1,10000) for x in range(size)] #Generating random values 1-10000
        product= list(values) #Dulicating the list

        print('Size list recording time:', size)

        time_decoratorA =decoratorA_bubble(values) #storing recording time for bubble_sort
        time_decoratorB= decoratorB_insertion(product) #storing recording time for insertion sort
        x_values.append(size) #append x values to list
        y_values_decoratorA.append(time_decoratorA) #append y values for bubble_sort to list
        y_values_decoratorB.append(time_decoratorB) #append y values for insertino_sort to list
    pyplot.plot(x_values, y_values_decoratorA, 'ro--', linewidth=2, label='Bubble Sort') #graph for bubble_sort
    pyplot.plot(x_values, y_values_decoratorB, 'go--', linewidth=2, label='Insertion Sort') #graph for insertion sort
    pyplot.legend(loc="upper left") #legend
    pyplot.show() #initiate showing graph


compare_sorts(sort_timer(bubble_sort), sort_timer(insertion_sort)) #test
