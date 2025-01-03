def compare_color_lists(list1, list2):
    # Print both lists
    print("List 1:", list1)
    print("List 2:", list2)
    
    # Find and print colors that are in list1 but not in list2
    unique_colors = [color for color in list1 if color not in list2]
    
    print("Colors in List 1 but not in List 2:")
    for color in unique_colors:
        print(color)

# Example usage:
list1 = ['red', 'blue', 'green', 'yellow', 'orange']
list2 = ['blue', 'yellow', 'purple']

compare_color_lists(list1, list2)

