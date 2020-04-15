def produce_fibonacci(x):
    fib = []
    for i in range(0, x):
        if i == 0 or i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib


def get_input(help_text="Enter your number: "):
    return int(input(help_text))


def compare_loop(user_input, main_list):  # compare with loop
    for element in main_list:
        if user_input == element:
            return True
    return False


def binary_search(input_element, ordered_list):  # compare with binary search (iterative)
    start_index = 0
    end_index = len(ordered_list)-1

    while (start_index <= end_index):
        middle_index = (start_index + end_index) // 2  # overflow can happen, but not important for this example

        if (input_element == ordered_list[middle_index]):
            return input_element
        if (input_element < ordered_list[middle_index]):
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    return False


if __name__ == '__main__':
    user_input = get_input("Number of elements in Fibonacci: ")
    a = produce_fibonacci(user_input)

    user_input = get_input()
    print(compare_loop(user_input, a))
    print(binary_search(user_input, a))
    print(a)
0


