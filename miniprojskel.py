# MINI PROJECT SKELETON: SIMPLE GRADE CALCULATOR
# This is the outline for students to fill in
# Each function is declared but empty - students add the code inside

def welcome_message():
    """Function to display welcome message"""
    # TODO: Print "STUDENT GRADE CALCULATOR" 
    # TODO: Print a line of equal signs (=) under the title
    # TODO: This function should make the program look professional
    pass

def get_test_scores():
    """Function to get three test scores from user"""
    # TODO: Ask the user to enter Test 1 score and convert to float
    # TODO: Ask the user to enter Test 2 score and convert to float  
    # TODO: Ask the user to enter Test 3 score and convert to float
    # TODO: Return all three scores (test1, test2, test3)
    pass

def calculate_average(score1, score2, score3):
    """Function to calculate average of three scores"""
    # TODO: Add all three scores together to get total
    # TODO: Divide the total by 3 to get the average
    # TODO: Return the average
    pass

def get_letter_grade(average):
    """Function to determine letter grade based on average"""
    # TODO: Use if-elif-else to check the average:
    # TODO: If average >= 90, return "A"
    # TODO: If average >= 80, return "B" 
    # TODO: If average >= 70, return "C"
    # TODO: Otherwise, return "F"
    pass

def display_result(test1, test2, test3, average, letter_grade):
    """Function to display grade results"""
    # TODO: Print a blank line for spacing
    # TODO: Print "Your Results:"
    # TODO: Print each test score with labels (Test 1: 85.0)
    # TODO: Print the average with 1 decimal place
    # TODO: Print the letter grade
    pass

def main():
    """Main function that runs the program"""
    # TODO: Call welcome_message() to start the program
    
    # TODO: Call get_test_scores() and store the returned values
    # HINT: Use test1, test2, test3 = get_test_scores()
    
    # TODO: Call calculate_average() with the three test scores
    # HINT: Store the result in a variable called avg
    
    # TODO: Call get_letter_grade() with the average
    # HINT: Store the result in a variable called grade
    
    # TODO: Call display_result() with all the information
    # HINT: Pass test1, test2, test3, avg, grade as arguments
    
    # TODO: Print a thank you message
    pass

# Run the program
if __name__ == "__main__":
    main()