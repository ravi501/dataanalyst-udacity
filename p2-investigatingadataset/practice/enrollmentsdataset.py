import unicodecsv
from datetime import datetime as dt


"""
Load data from CSVs
"""
def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')
print('Print CSV read data')
print enrollments[0]
print daily_engagement[0]
print project_submissions[0]


"""
Fixing data types
"""
# Takes a date as a string, and returns a Python datetime object.
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

def data_clean_up():
    # Clean up the data types in the enrollments table
    for enrollment in enrollments:
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
        enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
        enrollment['join_date'] = parse_date(enrollment['join_date'])


    # Clean up the data types in the engagement table
    for engagement_record in daily_engagement:
        engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
        engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
        engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
        engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
        engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

    # Clean up the data types in the submissions table
    for submission in project_submissions:
        submission['completion_date'] = parse_date(submission['completion_date'])
        submission['creation_date'] = parse_date(submission['creation_date'])


data_clean_up()

"""
Investigating the data
"""

## Find the total number of rows and the number of unique students (account keys)
## in each table.
def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

enrollment_num_rows = len(enrollments)
engagement_num_rows = len(daily_engagement)
submissions_num_rows = len(project_submissions)

unique_enrolled_students = get_unique_students(enrollments)
unique_engaged_students = get_unique_students(daily_engagement)
unique_submission = get_unique_students(project_submissions)

unique_enrolled_students_num = len(unique_enrolled_students)
unique_engaged_students_num = len(unique_engaged_students)
unique_submission_num = len(unique_submission)

print('The total number of rows and the number of unique students')
print enrollment_num_rows
print unique_enrolled_students_num

print engagement_num_rows
print unique_engaged_students_num

print submissions_num_rows
print unique_submission_num

"""
Problems in the data
"""
## Missing engagement records
## Find any one student enrollments where the student is missing from the daily engagement table.
## Output that enrollment.
print('============================')
print('Missing engagement records')
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engaged_students:
        print enrollment
        break

## Find the number of surprising data points (enrollments missing from
## the engagement table) that remain, if any.
num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engaged_students and enrollment['join_date'] != enrollment['cancel_date']:
        print enrollment
        num_problem_students += 1
print 'More surprising data points'
print num_problem_students

# Create a set of the account keys for all Udacity test accounts
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
len(udacity_test_accounts)

# Given some data with an account_key field, removes any records corresponding to Udacity test accounts
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

# Remove Udacity test accounts from all three tables
non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)
print 'Length of data points after removing udacity accounts'
print len(non_udacity_enrollments)
print len(non_udacity_engagement)
print len(non_udacity_submissions)


"""
Investigating the data further
"""
## Create a dictionary named paid_students containing all students who either
## haven't canceled yet or who remained enrolled for more than 7 days. The keys
## should be account keys, and the values should be the date the student enrolled.

paid_students = dict()

for enrollment in non_udacity_enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']

        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date
print 'Number of paid students'
print len(paid_students)







