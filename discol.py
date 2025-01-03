def display_colors(colors):
    # Display the first and last color
    if colors:  # Check if the list is not empty
        print("First color:", colors[0])
        print("Last color:", colors[-1])
        
        # Print each color in the list
        print("Colors in the list:")
        for color in colors:
            print(color)
    else:
        print("The list is empty.")

# Example usage:
colors_list = ['red', 'blue', 'green', 'yellow', 'orange']
display_colors(colors_list)

