"""Program for deciding weather or not a given year is a leap year
"""

def leap_year(year):
    """Function withc takes any year as a parameter and decides if its a leap year or not.
    returns a bool value 
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False   
        return True 
    return False
