from django.shortcuts import render
from datetime import datetime
import firebase_admin 
import json
from firebase_admin import firestore
import heapq as hp

# Create your views here.
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
    #return render(request, 'index.html', {'course_info': course_info})

def getOrderedByRank():
    heap = []

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
    print(heap)
    #return render(request, 'index.html', {'course_info': course_info})

calculateRank()
getOrderedByRank()