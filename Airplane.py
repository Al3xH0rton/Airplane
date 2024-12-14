from typing import List

def read_file(file_path: str) -> List[List[str]]:
    """Reads the seating data from a file."""
    seats = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                row = [item.strip() for item in line.split(',')]
                seats.append(row)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
    return seats

def print_seating_chart(seats: List[List[str]], num_rows: int):
    """Prints the current seating chart."""
    print("Current seating chart:")
    print(f"{' ' * 4}Seat -> {'A':<30}{'B':<30}{'C':<30}{'D':<30}")
    for i in range(num_rows):
        row_number = str(i + 1).zfill(2)
        print(f"Row {row_number}: {' ' * 4}{seats[i][0]:<30}{seats[i][1]:<30}{seats[i][2]:<30}{seats[i][3]:<30}")

def validate_seat_choice(seat_choice: str, num_rows: int) -> bool:
    """Validates the seat choice format."""
    if seat_choice == '99':
        return True  # Special case to end the process
    if len(seat_choice) < 2 or len(seat_choice) > 3:
        return False
    try:
        row = int(seat_choice[:-1])
        seat_letter = seat_choice[-1].upper()
        return 1 <= row <= num_rows and seat_letter in ['A', 'B', 'C', 'D']
    except ValueError:
        return False

def write_file(seats: List[List[str]], file_path: str):
    """Writes the updated seating chart back to a file."""
    try:
        with open(file_path, 'w') as myfile:
            for row in seats:
                myfile.write(','.join(row) + '\n')
        print("Seating chart saved successfully.")
    except IOError:
        print(f"Error: Unable to write to {file_path}.")

def assign_seat(seats: List[List[str]], row_num: int, seat_num: int, passenger: str):
    """Assigns a seat to a passenger."""
    if seats[row_num][seat_num] == "0":
        seats[row_num][seat_num] = passenger
        print(f"Seat {row_num + 1}{chr(seat_num + 65)} assigned to {passenger}.")
    else:
        print("Sorry, that seat is already taken.")
        response = input("Would you like to replace the current name? (Y/N): ").strip().lower()
        if response == 'y':
            seats[row_num][seat_num] = passenger
            print(f"Seat {row_num + 1}{chr(seat_num + 65)} reassigned to {passenger}.")
        else:
            print("Seat assignment skipped. Please choose another seat.")

def main():
    num_rows = int(input("How many rows? "))
    num_columns = int(input("How many columns? "))
    file_path = 'C:\\Users\\asira\\OneDrive\\Desktop\\Plane.txt'
    seats = read_file(file_path)
    
    if not seats or len(seats) < num_rows:
        print("Error: Invalid seating data.")
        return

    while True:
        print_seating_chart(seats, num_rows)
        seat_choice = input("Enter seat choice or '99' to end (e.g., 1A): ").strip()

        if seat_choice == '99'.strip():
            write_file(seats, file_path)
            break

        if not validate_seat_choice(seat_choice, num_rows):
            print("Invalid seat choice. Please try again.")
            continue

        passenger = input("Enter the passenger name: ").strip()
        row_num = int(seat_choice[:-1]) - 1
        seat_num = ord(seat_choice[-1].upper()) - 65
        assign_seat(seats, row_num, seat_num, passenger)

if __name__ == "__main__":
    main()