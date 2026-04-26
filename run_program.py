from square_of_even_and_cube_of_odd_integers import IntegerFileProcessor

processor = IntegerFileProcessor("integers.txt", "double.txt", "triple.txt")
processor.process_files()

print("Double.txt and triple.txt created successfully.")