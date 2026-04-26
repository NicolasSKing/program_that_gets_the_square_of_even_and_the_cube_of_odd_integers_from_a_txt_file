class IntegerFileProcessor:
    def __init__(self, input_file, even_output_file, odd_output_file):
        self.input_file = input_file
        self.even_output_file = even_output_file
        self.odd_output_file = odd_output_file

    def process_files(self):
        with open(self.input_file, 'r') as file:
            numbers = file.read().split()

        with open(self.even_output_file, 'w') as even_file, open(self.odd_output_file, 'w') as odd_file:
            for num in numbers:
                number = int(num)

                if number % 2 == 0:
                    even_file.write(str(num ** 2) + '\n')
                else:
                    odd_file.write(str(num ** 3) + '\n')
