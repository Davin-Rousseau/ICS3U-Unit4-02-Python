#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program uses a while loop
# To calculate the factorial of a given number


def main():
    # This function Calculates the factorial using a while loop
    loop_counter = 0
    answer = 1

    # input
    number = input("Enter a positive integer: ")
    print("")

    # process and output
    try:
        numberInput = int(number)
        while loop_counter < numberInput:
            print("{0} times through loop: ".format(loop_counter))
            loop_counter = loop_counter + 1
            answer = answer * loop_counter
        print("The factorial of the given number is: ", answer)
    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
