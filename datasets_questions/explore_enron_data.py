#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#poi_data = open("../final_project/poi_names.txt", "r")

poi_number  = sum(1 for data in enron_data.values() if data['poi'])
have_salary = sum(1 for data in enron_data.values() if data['total_payments'] != 'NaN' and data['poi'])
no_salary   = sum(1 for data in enron_data.values() if data['total_payments'] == 'NaN' and data['poi'])
print poi_number
print have_salary
print no_salary
print float(no_salary) / (have_salary+no_salary)
