def main():
    # Predefined list for demonstration
    my_list = [10, 20, 30, 40, 50, 20, 30, 20, 60]

    while True:
        print("\n--- List Operations Menu ---")
        print("1. Display List")
        print("2. Find Maximum Value")
        print("3. Find Minimum Value")
        print("4. Slice List")
        print("5. Count Occurrences of an Item")
        print("6. Find First Occurrence of an Item")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print("Current List:", my_list)

        elif choice == '2':
            if not my_list:
                print("List is empty.")
            else:
                print("Maximum value:", max(my_list))

        elif choice == '3':
            if not my_list:
                print("List is empty.")
            else:
                print("Minimum value:", min(my_list))

        elif choice == '4':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(f"Sliced List ({start}:{end}):", my_list[start:end])
            except ValueError:
                print("Invalid index input.")

        elif choice == '5':
            item = int(input("Enter item to count: "))
            count = my_list.count(item)
            print(f"The item {item} occurs {count} times.")

        elif choice == '6':
            item = int(input("Enter item to find: "))
            try:
                index = my_list.index(item)
                print(f"First occurrence of {item} is at index: {index}")
            except ValueError:
                print(f"Item {item} not found in the list.")

        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
