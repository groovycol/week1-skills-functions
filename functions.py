# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
def say_hello():
    """Print a message to the screen, return nothing"""
    
    #print to screen a hard-coded message
    print "Hello World."


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.
def greet_by_name(name):
    """Print a greeting to the variable name passed in. Returns nothing"""
    
    #print a message to the screen that contains the string passed in
    print "Hi " + name


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.
def multiply_nums(num1, num2):
    """multiply the 2 nums passed in and print the result. Return nothing."""
    
    #print the result of the 2 numbers passed in multiplied
    print num1 * num2


# 4. Write a function that takes a string and an integer and
#    prints the string that many times
def repeat_string(input_string, num):
    """Print the string passed in the number of times num passed in specifies. Return nothing"""
    
    #Repeat a print to screen of the string passed in the num of times passed in.
    print input_string * num


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".
def check_high_low(num):
    """Check the number passed in to see if it is 0, or higher or lower than 0. Return nothing"""
    
    #if the int passed in is equal to 0, print Zero to the screen
    if num == 0:
        print "Zero"
    #if the int passed in is greater than 0, print Higher to the screen
    elif num > 0:
        print "Higher than 0"
    #And in all other cases, the int must be less than zero, print Lower to the screen
    else:
        print "Lower than 0"


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.
def is_divisible_by_3(num):
    """takes the int passed in and checks to see if it is divisible by 3 using modulo. Return a boolean value"""
    
    #store the result of using modulo (%) 3 on the int passed in
    remainder = num % 3
    
    #if the result is equal to zero, the int passed in is evenly divisible by 3. return True
    if remainder == 0:
        return True
    #in all other cases, the result is not evenly divisible by three, so return False
    else:
        return False


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.
def find_num_spaces(input_string):
    """Return the number of spaces in the input_string passed in"""
    
    #start with a count of 0
    spaces_count = 0
    
    #iterate through the characters in the string, and increment the count if the char is a space
    for character in input_string:
        if character == " ":
            spaces_count += 1
    
    #return the total count of spaces
    return spaces_count

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.
def calculate_tip(bill_amt, tip=.15):
    """Return the total amt paid for a bill_amt passed in. Passing in a tip amt is optional, default is .15"""
    
    #return the result of the bill_amt plus the calculated tip amount. 
    #the parens are optional, but I added for clarity
    return float(bill_amt) + (float(bill_amt) * tip)

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
def find_num_properties(num):
    """For the int passed in, return a list of its properties(Even or Odd) and (Positive or Negative)"""
    
    #create an empty list to store properties
    property_list = []
    
    #if the number passed in is greater than 0, its sign is positive, else negative
    if num > 0:
        property_list.append("Positive")
    else:
        property_list.append("Negative")

    #if the number passed in can be evenly divided by 2, its parity is even, else odd
    if num % 2 == 0:
        property_list.append("Even")
    else:
        property_list.append("Odd")

    #return the list containing sign and parity
    return property_list
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

def calculate_tax(state,item_price,tax=.05):
    """Return the total cost of an item with tax. If state is CA, override the tax default amount"""

    #check the state, if it's California, change the default value of tax
    if state == "CA":
        tax=.07
    #return the total price which is calculated as item price + item_price * tax
    #parens aren't necessary, but used for clarity
    return float(item_price) + (float(item_price) * tax)


# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.
def print_name_and_job(name,job_title="Engineer"):
    """Print the passed in name and job title. Use the default value of job_title if not passed in. Return nothing"""
    print job_title + " " + name

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

#test functions
say_hello()
greet_by_name(name="Bonnie")
multiply_nums(num1=3, num2=9)
repeat_string(input_string="Good day, Sir!", num=4)
check_high_low(num=0)
check_high_low(num=-4)
check_high_low(num=5)
print is_divisible_by_3(num=27)
print is_divisible_by_3(num=4)
print find_num_spaces(input_string="The rain in Spain falls mainly on the plains")
print find_num_spaces(input_string="Cumberbatch")
print calculate_tip(bill_amt=75.50)
print calculate_tip(bill_amt=125.70, tip=.20)
print calculate_tip(bill_amt=98, tip=.18)
sign, parity = find_num_properties(num=5)
print sign + " " + parity
sign, parity = find_num_properties(num=-2)
print sign + " " + parity
print calculate_tax(state="CA", item_price=100.00)
print calculate_tax(state="DE", item_price=50, tax=0)
print calculate_tax(state="MD", item_price=50.50)
print_name_and_job(name="Veronica", job_title="Cheerleader")
print_name_and_job(name="Betty")
