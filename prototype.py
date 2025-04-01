from datetime import datetime
import json

today_date = datetime.today().strftime('%d/%m/%Y')

training_data = {
}


def add_record(user_id, date, exercise, weight, sets, reps):
    # Generate a unique record_id (increment from the last one)
    new_id = max([record["record_id"] for record in training_data.get(user_id, [])], default=0) + 1

    # Create a new record dictionary
    new_record = {
        'record_id': new_id,
        'date': date,
        'exercise': exercise,
        'weight': weight,
        'sets': sets,
        'reps': reps
    }

    # If user exists, append to their list
    if user_id in training_data:
        training_data[user_id].append(new_record)
    else:
        # If user doesn't exist, create a new list with the record
        training_data[user_id] = [new_record]


def show_records(user_id):
    if user_id in training_data and training_data[user_id]:
        print(f"\n Records for User {user_id}:")
        for record in training_data[user_id]:
            print(
                f"Record ID: {record['record_id']}, Date: {record['date']}, Exercise: {record['exercise']}, Weight: {record['weight']}, Sets: {record['sets']} Reps: {record['reps']} ")
    else:
        print(f"No records found for User {user_id}")


def delete_record(user_id, record_id):
    if user_id in training_data:
        original_len = len(training_data[user_id])
        updated_records = [record for record in training_data[user_id] if record['record_id'] != record_id]

        if len(updated_records) < original_len:
            training_data[user_id] = updated_records  # <-- move this inside the if block
            print(f"✅ Record {record_id} deleted for User {user_id}")
        else:
            print(f"no record {record_id} found for the user {user_id}")
    else:
        print(f"No user found {user_id}")


while True:
    print("1, Add Record")
    print("2, Show Records")
    print("3, Delete Records")
    print("4, Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":
        user_id = input("Enter User ID: ")
        date = today_date
        exercise = input("Enter exercise: ")
        weight = input("Enter weight: ")
        sets = input("Enter sets: ")
        reps = input("Enter reps: ")
        add_record(user_id, date, exercise, weight, sets, reps)

    elif user_choice == "2":
        user_id = input("Enter User ID to view records: ")
        show_records(user_id)

    elif user_choice == "3":
        user_id = input("Enter User ID: ")
        record_id = input("Enter Record ID to delete: ")
        delete_record(user_id, record_id)

    elif user_choice == "4":
        print("exit")
        break

"""
add_record(101, "2025-03-17", "Deadlift", 180, 5)
add_record(101, "2025-03-17", "sqaut", 180, 5)
add_record(102, "2025-03-17", "Deadlift", 180, 5)

formatted_users = json.dumps(training_data, indent=4)
print(formatted_users)
"""
