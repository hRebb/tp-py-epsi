# instanciez la liste suivante
# list = [1990, 1996, 1994, 1997, 1993, 2001, 1999, 2000]

# Affichez le 2ème plus petit élément (astuce : en supprimant le plus petit, le 2ème plus petit devient à son tour le plus petit)

def second_smallest(numbers):
    # Initialize the two smallest variables to infinity
    smallest = float('inf')
    second_smallest = float('inf')
    
    # Loop through each number in the list
    for num in numbers:
        # If the current number is smaller than the smallest number so far,
        # update the smallest and second smallest variables accordingly
        if num <= smallest:
            second_smallest = smallest
            smallest = num
        # If the current number is larger than the smallest number so far but
        # smaller than the second smallest number so far, update the second
        # smallest variable accordingly
        elif num < second_smallest:
            second_smallest = num
    
    # Return the second smallest number
    return second_smallest

print(second_smallest([1990, 1996, 1994, 1997, 1993, 2001, 1999, 2000]))