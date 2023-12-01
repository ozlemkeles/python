"""
Counts the number of nearly similar rectangles in a given list of rectangles.

Two rectangles are considered nearly similar if the ratio of their sides is the same.

Parameters:
sides (list of lists): List of rectangles represented by their sides.

Returns:
int: The count of nearly similar rectangles.
"""

def nearlySimilarRectangles(sides):

    # A dictionary to store the count of sides ratios
    sides_ratios_count = {}

    # Count of nearly similar rectangles
    count_nearly_similar = 0

    for rectangle in sides:
        # Calculate the sides ratio
        ratio = rectangle[0] / rectangle[1]

        # Check if the ratio is already encountered
        if ratio in sides_ratios_count:
            # If encountered, update the count
            count_nearly_similar += sides_ratios_count[ratio]

            # Increment the count for the current ratio
            sides_ratios_count[ratio] += 1
        else:
            # If the ratio is not encountered, add it to the dictionary
            sides_ratios_count[ratio] = 1

    return count_nearly_similar

sides = [
    [4, 2],
    [6, 3],
    [2, 4],
    [5, 10],
]

result = nearlySimilarRectangles(sides)
print("Count of nearly similar rectangles:", result)