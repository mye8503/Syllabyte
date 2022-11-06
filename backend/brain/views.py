from django.shortcuts import render
from datetime import datetime
import firebase_admin 
import json
from rest_framework import response
import heapq as hp
import time

# Dummy data
course_info = {
        'APS360': {
            'priority': 1,
            'Assignments': {
                'Lab': {
                    'number': 4,
                    'percentage': 3,
                    'due': '2022-08-11',
                    'time_needed': 6,
                    'time_spent': 4,
                    'rank': 0,
                    'state': 1
                },
                'progress_report': {
                    'number': 1,
                    'percentage': 10,
                    'due': '2022-12-11',
                    'time_needed': 2,
                    'time_spent': 0,
                    'rank': 0,
                    'state': 1
                }
            },
            'Exams': {}
        },
        'ECE344': {
            'priority': 3,
            'Assignments': {
                'Lab': {
                    'number': 4,
                    'percentage': 6,
                    'due': '2022-08-11',
                    'time_needed': 10,
                    'time_spent': 2,
                    'rank': 0,
                    'state': 1
                }
            },
            'Exams': {
                'Quiz': {
                    'number': 1,
                    'percentage': 12,
                    'due': '2022-13-11',
                    'time_needed': 14,
                    'time_spent': 1,
                    'rank': 0,
                    'state': 1
                }
            }
        },
        'ECE345': {
            'priority': 2,
            'Assignments': {
                'Homework': {
                    'number': 2,
                    'percentage': 5,
                    'due': '2022-10-11',
                    'time_needed': 2,
                    'time_spent': 0,
                    'rank': 0,
                    'state': 1
                }
            },
            'Exams': {
                'Midterm': {
                    'number': 1,
                    'percentage': 35,
                    'due': '2022-20-11',
                    'time_needed': 14,
                    'time_spent': 2,
                    'rank': 0,
                    'state': 1
                }
            }
        }
    }
heap = []
# calulate rank for each assignment
def calculateRank():
    priority = 0
    for course in course_info:
        course_struct = course_info[course]

        for item in course_struct:
            name = item
            item = course_struct[item]
            if(type(item) != dict):
                priority = item
            else:
                for sub_item in item:
                    sub_item = item[sub_item]

                    days_remaining = (datetime.strptime(sub_item['due'], '%Y-%d-%m') - datetime.today()).days

                    if(sub_item['time_needed'] >= days_remaining):

                        if(days_remaining == 0): days_remaining = 0.5
                        sub_item['rank'] = sub_item['percentage'] * ((sub_item['time_needed'] - sub_item['time_spent'])/days_remaining) * priority/len(course_struct)
                        
                    else:
                        sub_item['rank'] = 0

# get ordered assignments in a list
def getOrderedByRank(course_name='ECE344', priority='nil', state='nil', assignment_name='nil', number = 'nil'):
    if(priority != 'nil'):
        setPriorities(course_name, priority)

    if(state != 'nil'):
        setStates(course_name, assignment_name, state)

    heap = []
    calculateRank()

    for course in course_info:
        course_struct = course_info[course]
        for item in course_struct:
            item = course_struct[item]
            if(type(item) != dict):
                continue
            else:
                for sub_item in item:
                    name = sub_item
                    sub_item = item[sub_item]
                    assignment_info = {
                        'rank': sub_item['rank'],
                        'course': course,
                        'assignment': name + ' ' + str(sub_item['number']),
                        'dueIn': (datetime.strptime(sub_item['due'], '%Y-%d-%m') - datetime.today()).days,
                        'state': sub_item['state']
                    }
                    heap.append((assignment_info['rank'], assignment_info))
    heap = sorted(heap, key=lambda x: x[0], reverse=True)
    printAll(heap)
    

def setPriorities(course_name, priority):
    priority = int(priority)
    if(priority > 1 or priority < -1):
        return ('invalid priority')

    priority_num = course_info[course_name]['priority']
    for course in course_info:
        course_struct = course_info[course]
        for item in course_struct:
            item = course_struct[item]

            if(type(item) != dict):
                if(course == course_name):
                    course_info[course]['priority'] += priority
                if(course_struct['priority'] > priority_num):
                    course_info[course]['priority'] -= priority

def setStates(course_name, assignment_name, state):
    if(state > 3 and state < 1):
        return response('invalid state')
    
    for course in course_info:
        course_struct = course_info[course]
        if(course == course_name):
            for item in course_struct:
                name = item
                item = course_struct[item]
                for sub_item in item:
                    if(sub_item == assignment_name):
                        item[sub_item]['state'] = state
                        return response('state changed')

    
    return response('failed')

# print all tasks
def printAll(data_struct):
    for i in range(len(data_struct)):
        print("--------------------------")
        print(data_struct[i][1]['course'], "-->", data_struct[i][1]['assignment'], "due in: ", data_struct[i][1]['dueIn'], "days ", "ranked: ", data_struct[i][1]['rank'])
        print("--------------------------")
        print("            ^")
        print('            |')
        print('            |')

while(True):
    print('your tasks in order of priority:')
    getOrderedByRank()

    coursename, priority = input('set priority for a course - (format) course name (ECE344, ECE345, ECE346) priority (1, 0, -1) :     ').split()
    getOrderedByRank(coursename, priority)

    wait = input('press 1 to refresh')
    time.sleep(int(wait))

