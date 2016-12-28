import unicodecsv
import pandas as pd
import matplotlib.pyplot as plt

"""
Load Data from CSVs

The first step in the process would be to load the data from the CSV file into our data dictionary.
"""
def read_csv_file(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

titanic_data_pandas = pd.read_csv('titanic-data.csv')

print('Using describe method to print the description of the data')
print titanic_data_pandas.describe()

print('Printing the actual data')
print titanic_data_pandas

"""
Data Wrangling Phase

Once the CSV data is imported into the lists, the data needs to be fixed and the data needs to be converted into
their respective data types.
"""
# Takes string with values 0 or 1,
# and returns a boolean True or False
def parse_int_to_boolean(i):
    if i == 1:
        return True
    elif i == 0:
        return False

# Takes the name of the passenger, and returns the first name and last name
# as a list. This function also removes the Mr., Mrs., Miss, Master titles given to the person,
# and it also crops out everything provided in brackets
def parse_first_and_last_names(name):

    #Splits the name by a comma
    first_last_names = name.split(",")

    #Splits the first name by ". "
    first_last_names[1] = first_last_names[1].split(". ")[1]

    #If the name contains anything in brackets, they are ignored
    if '(' in first_last_names[1]:
        first_last_names[1] = first_last_names[1].split(" (")[0]
    return first_last_names[0], first_last_names[1]

# Takes the sex as male or femal, and returns a single character 'M' or 'F'
def parse_sex(sex):
    if 'male' == sex:
        return 'M'
    else:
        return 'F'

def get_last_names(name):
    return name[0]


titanic_data_pandas['Name'] = titanic_data_pandas['Name'].map(parse_first_and_last_names)
titanic_data_pandas['Sex'] = titanic_data_pandas['Sex'].map(parse_sex)
titanic_data_pandas['Survived'] = titanic_data_pandas['Survived'].map(parse_int_to_boolean)
titanic_data_pandas['Last Name'] = titanic_data_pandas['Name'].map(get_last_names)

print('Printing the titanic data after performing cleaning operations')
print titanic_data_pandas

"""
Exploration, Conclusions and Communication Phase

"""

## 1. The ratio of male to female survivors
def male_female_survivors_ratio():
    male_female_survivors = titanic_data_pandas.groupby('Sex')['Survived'].count()
    labels = 'Male', 'Female'
    colors = ['yellow', 'blue']
    plt.title('Ratio of male to female survivors')
    plt.pie(male_female_survivors, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
    plt.show()

male_female_survivors_ratio()

## 2. The ratio of first, second and third class survivors
def class_wise_survivors():
    first_second_third_class_survivors = titanic_data_pandas.groupby('Pclass')['Survived'].count()

    labels = 'First class', 'Second class', 'Third class'
    colors = ['yellow', 'blue', 'Green']
    plt.title('Ratio of first, second and third class survivors')
    plt.pie(first_second_third_class_survivors, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
    plt.show()

class_wise_survivors()

## 3. The ratio of passengers who survived vs those who didn't in first, second and third classes
def survivors_vs_non_survivors():
    each_class_survivors = titanic_data_pandas.groupby(['Survived', 'Pclass']).size().unstack('Survived').fillna(False)

    each_class_survivors[[0, 1]].plot(kind='bar')
    plt.title('Survivors by class')
    plt.xlabel('Class numbers')
    plt.ylabel('Survived vs not survived count')
    plt.show()

survivors_vs_non_survivors()

## 4. Survived passengers grouped by last name
def survivors_grouped_by_last_name():
    survivors_by_last_name = titanic_data_pandas.groupby('Last Name')['Survived'].count()

    labels1 = titanic_data_pandas['Last Name'].unique()

    plt.pie(survivors_by_last_name, labels=labels1, shadow=True)
    print plt.show()

survivors_grouped_by_last_name()