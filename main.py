# I have created a function called calendar that shows a range from the
# first element (calendar_1) to the last element (calendar_2) + 1 so
# it can print even the last requested year
def calendar(calendar_1, calendar_2):
    calendar_range = list(range(calendar_1, calendar_2 + 1))
    return calendar_range


# Bellow are initialised 2 variables where the user enter the starting year
# and the finishing year of his range.
user_input_1 = int(input("Please type the first year from your range -> "))
user_input_2 = int(input("Please type the last year from your range -> "))
user_range = calendar(user_input_1, user_input_2)
print(user_range)
