class FibonacciSeriesGenerator:

    def FibonacciSeriesGenerator(self):
        pass

    def basic_fibonacci_series(self, series_length):
        first_num, second_num = 0, 1
        counter = 0
        while counter < series_length:
            print(first_num, end=' ')
            first_num, second_num = second_num, first_num + second_num
            counter += 1

    def fibonacci_series_to_number(self, series_last_number):
        first_num, second_num = 0, 1
        while first_num < series_last_number:
            print(first_num, end=' ')
            first_num, second_num = second_num, first_num + second_num


fibonacciSeriesGenerator = FibonacciSeriesGenerator()
# series_length = int(input("Enter length of your fibonacci series "))
# fibonacciSeriesGenerator.basic_fibonacci_series(series_length)

series_last_number = int(input("Enter last number of your fibonacci series "))
fibonacciSeriesGenerator.fibonacci_series_to_number(series_last_number)
