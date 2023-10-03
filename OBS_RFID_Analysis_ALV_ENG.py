import time

# Specify the path to the location where you have saved your txt files
path = '/Users/alessandroloverde/Desktop/Github/Python-Database-OBS-RFID/OBS_data.txt'
path2 = '/Users/alessandroloverde/Desktop/Github/Python-Database-OBS-RFID/RFID_data.txt'

# The function takes the directory where the file is located as input
# and creates a dictionary where the keys are the column headers of the dataset
# and the values in each column.

def reading_function(path):
    variables = {}  # Create a dictionary to store variables
    with open(path, 'r') as f:
        rows = f.readlines()
        header = rows[0].strip().split('\t')  # Extract the header
        for i in header:
            variables[i] = []  # Initialize an empty list to store the columns

        for row in rows[1:]:  # Start from the second row
            data = row.strip().split('\t')
            for j in range(len(header)):
                variables[header[j]].append(data[j])  # Add the data to the corresponding list

    return variables

# Use our function to read the two files
OBS = reading_function(path)
RFID = reading_function(path2)
# Access OBS variables
datetimeOBS = OBS["DateTime"]
actor = OBS["Actor"]
recipient = OBS["Recipient"]
behavior = OBS["Behavior"]
category = OBS["Category"]
duration = OBS["Duration"]
point = OBS["Point"]

# Save RFID variables
t = RFID["t"]
first_i = RFID["i"]
second_j = RFID["j"]
datetimeRFID = RFID["DateTime"]

"""
PART A

Using the OBS DATA file.

Define useful functions to perform the exercises.

"""

# Function that counts elements from a list
def count_list(list1, list_to_count=None, duplicates=True, count=None):
    # Create a dictionary for counting
    if count is None:
        count = {}
    # Count elements in the list
    if list_to_count is None:
        list_to_count = [1] * len(list1)
    # If duplicates is True, count for identical elements
    if duplicates == True:
        for i in range(len(list1)):
            if list1[i] != '':
                count[list1[i]] = count.get(list1[i], 0) + int(list_to_count[i])
    else:
        for i in range(len(list1)):
            # Count each individual element in list_to_count
            if list1[i] != '':
                if list1[i] in count:
                    count[list1[i]].add(list_to_count[i])
                else:
                    count[list1[i]] = {list_to_count[i]}

    return count

def count_two_lists(list1, list2, list_to_count=None, duplicates=True, couple=False):
    # Create dictionaries for counting
    count = {}
    # Count elements in the list
    if list_to_count is None:
        list_to_count = [1] * len(list1)
    if couple == True:
        # Count in pairs
        if duplicates == True:
            for i in range(len(list1)):
                if list1[i] != '' and list2[i] != '':
                    couple = tuple(sorted([list1[i], list2[i]]))
                    if couple in count:
                      count[couple] += int(list_to_count[i])
                    else:
                      count[couple] = int(list_to_count[i])
        else:
            for i in range(len(list1)):
                if list1[i] != '' and list2[i] != '':
                    couple = tuple(sorted([list1[i], list2[i]]))
                    if couple in count:
                        count[couple].add(list_to_count[i])
                    else:
                        count[couple] = {list_to_count[i]}
    else:
        # Count the lists
        if duplicates == True:
          count = count_list(list1, list_to_count, duplicates=True)
          count = count_list(list2, list_to_count, duplicates=True, count=count)
        else:
          count = count_list(list1, list_to_count, duplicates=False)
          count = count_list(list2, list_to_count, duplicates=False, count=count)

    return count

# Function that returns the maximum frequency and the corresponding element from an input count dictionary
def find_max(count, duplicates=True):
    # Find the element with the maximum count
    max_freq = 0  # Initialize the maximum count to 0
    max_elements = []  # Initialize the list of elements

    if duplicates == True:  # If duplicates is True, count identical elements multiple times
        for element, count in count.items():
            if count > max_freq:
                # If the current count is greater than the previous maximum count,
                # update the maximum count and reset the list of maximum elements.
                max_freq = count
                max_elements = [element]
            elif count == max_freq:
                # If the current count is equal to the previous maximum count,
                # add the element to the list of maximum elements.
                max_elements.append(element)
    else:  # If duplicates is False, handle unique elements
        for element, count in count.items():
            count = len(count)  # Calculate the count as the length of the current element
            if count > max_freq:
                # If the current count is greater than the previous maximum count,
                # update the maximum count and reset the list of maximum elements.
                max_freq = count
                max_elements = [element]
            elif count == max_freq:
                # Handle potential ties
                max_elements.append(element)

    return max_freq, max_elements  # Return the maximum count and the list of maximum elements

# Function that returns the maximum frequency and the corresponding element from an input list
def most_frequent(list, list_to_count=None, duplicates=True):
    # Call the function to count the list
    count = count_list(list, list_to_count, duplicates)
    # Call the function to find the most frequent element
    [max_freq, max_element] = find_max(count, duplicates)

    return max_freq, max_element

# Function that returns the maximum frequency and the corresponding element from two input lists
def most_frequent_two_lists(list1, list2, list_to_count=None, duplicates=True, couple=False):
    # Call the function to count two lists
    count = count_two_lists(list1, list2, list_to_count, duplicates, couple)

    # Call the function to find the most frequent element
    max_freq, max_element = find_max(count, duplicates)

    return max_freq, max_element

"""

1.  Which primate has been involved in the most events both as an "Actor" and as a "Recipient"?

"""

start = time.time()
# Find the primate that appears most frequently as an actor and recipient
[max_freq, max_primate] = most_frequent_two_lists(actor, recipient)
end = time.time()

# Print the result
print("1. The primate that has been involved the most both as an actor and as a recipient is "
       + str(max_primate) + ", which has been involved in " + str(max_freq) + " events.\n")
print(end-start)

"""

2.  Which primate has been involved in the most events as an "Actor"?

"""

start = time.time()
# Find the primate that appears most frequently as an Actor
[max_freq, max_primate] = most_frequent(actor)
end = time.time()

# Print the result
print("2. The primate that has been involved the most as an actor is "
       + str(max_primate) + ", which has been involved in " + str(max_freq) + " events.\n")
print(end-start)

"""

3.  Which primate has been involved in the most events as a "Recipient"?

"""

start = time.time()
# Find the primate that appears most frequently as a Recipient
[max_freq, max_primate] = most_frequent(recipient)
end = time.time()

# Print the result
print("3. The primate that has been involved the most as a recipient is "
       + str(max_primate) + ", which has been involved in " + str(max_freq) + " events.\n")
print(end-start)

"""

4.  What is the day with the most events?

"""

# Function that separates date and time
def separate_date_time(list):
    date = []
    time = []

    for element in list:
        # Separation of date and time
        d, t = element.split(' ')

        # Add to the date list
        date.append(d)

        # Add to the time list
        time.append(t)

    return date, time

start = time.time()
[data_OBS, time_OBS] = separate_date_time(datetimeOBS)
end = time.time()
print(end-start)

start = time.time()
# Find the day with the most events
[max_freq, max_day] = most_frequent(data_OBS)
end = time.time()

# Print the result
print("4. The day with the most events is " + str(max_day) + " on which "
      + str(max_freq) + " events occurred.\n")
print(end-start)

"""

5.  What is the hour of the day with the most events?

"""

# Function that separates hours and minutes
def separate_hours_minutes(list):
    hours = []
    minutes = []

    for element in list:
        # Separation of hours and minutes
        hour, minute = element.split(':')

        # Add to the hours list
        hours.append(hour)

        # Add to the minutes list
        minutes.append(minute)

    return hours, minutes

start = time.time()
[hours_OBS, minutes_OBS] = separate_hours_minutes(time_OBS)
end = time.time()
print(end-start)

start = time.time()
# Find the hour of the day with the most events
[max_freq, max_hour] = most_frequent(hours_OBS)
end = time.time()

# Print the result
print("5. The hour of the day with the most events is " + str(max_hour) + " in which "
       + str(max_freq) + " events occurred.\n")
print(end-start)

"""

6.  What is the most recorded behavior?

"""
start = time.time()
# Find the most recorded behavior
[max_freq, max_behavior] = most_frequent(behavior)
end = time.time()

# Print the result
print("6. The most frequent behavior is " + str(max_behavior) + ", which was observed " + str(max_freq) + " times.\n")
print(end-start)

"""

7.  What is the pair of primates involved together in the most events?

"""
start = time.time()
# Find the pair of primates involved in the most events together
[max_freq, max_couple] = most_frequent_two_lists(actor, recipient, couple=True)
end = time.time()

# Print the result
print("7. The pair of primates that has been involved in the most events is " + str(max_couple)
      + ", which has been involved in " + str(max_freq) + " events.\n")
print(end-start)

"""

8.  Which primate has been involved the longest in events both as an "Actor" and as a "Recipient"? (counting durations)

"""

start = time.time()
# Find the primate that has been involved the longest both as an actor and as a recipient
[max_freq, max_primate] = most_frequent_two_lists(actor, recipient, duration)
end = time.time()

# Print the result
print("8. The primate that has been involved the longest both as an actor and as a recipient is "
       + str(max_primate) + ", which has been involved for " + str(max_freq) + " seconds.\n")
print(end-start)

"""

9.  Which primate has been involved the longest as an "Actor"? (counting durations)

"""
start = time.time()
# Find the primate that has been involved the longest as an Actor
[max_freq, max_primate] = most_frequent(actor, duration)
end = time.time()

# Print the result
print("9. The primate that has been involved the longest as an actor is "
       + str(max_primate) + ", which has been involved for " + str(max_freq) + " seconds.\n")
print(end-start)

"""

10.  Which primate has been involved the longest as a "Recipient"? (counting durations)

"""

start = time.time()
# Find the primate that has been involved the longest as a Recipient
[max_freq, max_primate] = most_frequent(recipient, duration)
end = time.time()

# Print the result
print("10. The primate that has been involved the longest as a recipient is "
      + str(max_primate) + ", which has been involved for " + str(max_freq) + " seconds.\n")
print(end-start)

"""

11.  What is the pair of primates involved together the longest (in more events counting durations)?

"""
start = time.time()
# Find the pair of primates involved in events with the longest cumulative duration
[max_freq, max_couple] = most_frequent_two_lists(actor, recipient, duration, couple=True)
end = time.time()

# Print the result
print("11. The pair of primates that has been involved in the most events is " + str(max_couple)
      + ", which has been involved for " + str(max_freq) + " seconds.\n")
print(end-start)

"""

12.  Which primate has the most different behaviors? If A is involved twice in the "Playing with" behavior, this counts as one.

"""
start = time.time()
# Find the primate with the most different observed behaviors
[max_freq, max_primate] = most_frequent(actor, behavior, duplicates=False)
end = time.time()

# Print the result
print("12. The primate with the most different observed behaviors is " + str(max_primate)
      + ", which has shown " + str(max_freq) + " different behaviors.\n")
print(end-start)

"""

13.  What is the pair of primates involved together in the most different events? If A and B are involved twice in the "Playing with" behavior, this counts as one.

"""
start = time.time()
# Find the pair of primates involved in the most different events
[max_freq, max_couple] = most_frequent_two_lists(actor, recipient, behavior, duplicates=False, couple=True)
end = time.time()

# Print the result
print("13. The pair of primates that has been involved in the most different behaviors is " + str(max_couple)
      + ", which has been involved in " + str(max_freq) + " different behaviors.\n")
print(end-start)

"""

14.  What is the day with the most different behaviors? If the "Playing with" behavior appears twice in a day, this counts as one.

"""
start = time.time()
# Find the day with the most different observed behaviors
[max_freq, max_day] = most_frequent(data_OBS, behavior, duplicates=False)
end = time.time()

# Print the result
print("14. The days on which the most different behaviors were observed are " + str(max_day) + " on which "
      + str(max_freq) + " different behaviors were observed.\n")
print(end-start)

# PART B Using the RFID DATA file

"""

1.  Which pair of primates is involved together in the most interactions?

"""

start = time.time()
# Find the pair of primates involved together in the most interactions
[max_freq, max_couple] = most_frequent_two_lists(first_i, second_j, couple=True)
end = time.time()

# Print the result
print("2.1 The pair of primates that has been involved in the most interactions is " + str(max_couple)
       + ", which has been involved in " + str(max_freq) + " interactions.\n")
print(end-start)

"""

2.  Which primate is involved in the most interactions?

"""

start = time.time()
# Find the primate that is involved in the most interactions
[max_freq, max_primate] = most_frequent_two_lists(first_i, second_j)
end = time.time()

# Print the result
print("2.2 The primate that has been involved in the most interactions is "
      + str(max_primate) + ", which has been involved in " + str(max_freq) + " interactions.\n")
print(end-start)

"""

3.  Which primate has interactions on the most days? If a day has more interactions, the day counts as one.

"""

start = time.time()
# Separate the DateTime list into date and time
[data_RFID, time_RFID] = separate_date_time(datetimeRFID)
end = time.time()

# Find the primate that has interactions on the most different days
[max_freq, max_primate] = most_frequent_two_lists(first_i, second_j, data_RFID, duplicates=False)

# Print the result
print("2.3 The primates that have had the most interactions on the most different days are "
       + str(max_primate) + ", which have been involved for " + str(max_freq) + " days.\n")
print(end-start)

"""

4.  Which pair of primates has interactions on the most different days? If they have more interactions on a day, the day counts as one.

"""

start = time.time()
# Find the pair of primates involved together in the most different days
[max_freq, max_couple] = most_frequent_two_lists(first_i, second_j, data_RFID, duplicates=False, couple=True)
end = time.time()

# Print the result
print("2.4 The pairs of primates that have had interactions on the most different days are " + str(max_couple)
      + ", which have been involved on " + str(max_freq) + " different days. \n")
print(end-start)

"""

5.  What is the day with the most interactions?

"""

start = time.time()
# Find the day with the most interactions
[max_freq, max_day] = most_frequent(data_RFID)
end = time.time()

# Print the result
print("2.5 The day with the most interactions is " + str(max_day) + " on which "
      + str(max_freq) + " interactions occurred.")

print(end-start)

