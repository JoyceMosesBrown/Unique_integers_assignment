def extract_and_sort_unique_integers(source_file_path):
    unique_sorted_integers = []
    with open(source_file_path, 'r') as file:
        for line in file:
            try:
                number = int(line.strip())
                if -1023 <= number <= 1023:  # Check if the number falls within the specified range
                    unique_sorted_integers = insert_in_sorted_order(unique_sorted_integers, number)
            except ValueError:
                continue
    return unique_sorted_integers

def insert_in_sorted_order(sorted_list, value):
    #Insert value into sorted_list while maintaining the sorted order.
    if value in sorted_list:
        return sorted_list  # Avoid duplicate entries
    for i in range(len(sorted_list)):
        if value < sorted_list[i]:
            sorted_list = sorted_list[:i] + [value] + sorted_list[i:]
            return sorted_list
    sorted_list.append(value)
    return sorted_list

def save_integers_to_file(destination_file_path, integers):
    #Write each integer from the list to the specified file, one per line.
    with open(destination_file_path, 'w') as file:
        for integer in integers:
            file.write(f"{integer}\n")


def handle_file_operations(source_file_path, destination_file_path):
    #Handle the process of reading, sorting, and writing unique integers.
    unique_sorted_integers = extract_and_sort_unique_integers(source_file_path)
    save_integers_to_file(destination_file_path, unique_sorted_integers)

# Example usage
source_file = 'sample_input_for_students\small_sample_input_04.txt'
destination_file = 'sample_results_for_students\small_sample_results_04.txt'
handle_file_operations(source_file, destination_file)
