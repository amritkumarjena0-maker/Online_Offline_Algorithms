# Main Program: Online and Offline Algorithms

from online_load_balancing import online_load_balancing
from matrix_chain_multiplication import matrix_chain_multiplication

while True:
    print("\n===== ONLINE AND OFFLINE ALGORITHMS =====")
    print("1. Online Load Balancing")
    print("2. Matrix-Chain Multiplication")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        online_load_balancing()

    elif choice == "2":
        matrix_chain_multiplication()

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")