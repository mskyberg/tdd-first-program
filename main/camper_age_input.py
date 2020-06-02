"""
Program: camper_age_input.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: demonstrate function call and tdd development
"""

# constant for number of months in one year
MONTHS = 12


# function to convert years to months
def convert_to_months(years):
    return years * MONTHS


if __name__ == '__main__':
    # prompt the user for age input
    age_in_years = input('Please input your camper age in years:')
    # cast the user input into an integer for converting
    age_in_years = int(age_in_years)
    # convert years to months
    age_in_months = convert_to_months(age_in_years)
    # output both years and months of user input
    print('Your camper age of ' + str(age_in_years) +
          ' years is ' + str(age_in_months) + ' months old')
