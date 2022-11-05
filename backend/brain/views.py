from pprint import PrettyPrinter
from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import viewsets
=======
from datetime import datetime
import json
>>>>>>> f734861 (made algo using dummy data)

class ListView(viewsets.ModelViewSet):
    pass
    # create a serializer class and
    # assign it to the TodoSerializer class
    
# Create your views here.
course_info = {
        'APS360': {
            'priority': 1,
            'Assignments': {
                'Lab': {
                    'number': 4,
                    'percentage': 3,
                    'due': '2022-07-11',
                    'time_needed': 6,
                    'time_spent': 4,
                    'rank': 0
                },
                'progress_report': {
                    'number': 1,
                    'percentage': 10,
                    'due': '2022-12-11',
                    'time_needed': 2,
                    'time_spent': 0,
                    'rank': 0
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
                    'rank': 0
                }
            },
            'Exams': {
                'Quiz': {
                    'number': 1,
                    'percentage': 12,
                    'due': '2022-13-11',
                    'time_needed': 14,
                    'time_spent': 1,
                    'rank': 0
                }
            }
        },
        'ECE345': {
            'priority': 3,
            'Assignments': {
                'Homework': {
                    'number': 2,
                    'percentage': 5,
                    'due': '2022-06-11',
                    'time_needed': 2,
                    'time_spent': 0,
                    'rank': 0
                }
            },
            'Exams': {
                'Midterm': {
                    'number': 1,
                    'percentage': 35,
                    'due': '2022-20-11',
                    'time_needed': 14,
                    'time_spent': 2,
                    'rank': 0
                }
            }
        }
    }
def calculateRank():
    priority = 0
    for course in course_info:
        course_struct = course_info[course]

        for item in course_struct:
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
                        print(type(sub_item['percentage']))
                    else:
                        sub_item['rank'] = 0
                    print("rank: ", sub_item['rank'], "for ", item)

            
                
calculateRank()