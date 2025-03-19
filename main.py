from datetime import datetime
import json

today_date = datetime.today().strftime('%d/%m/%Y')

training_data = {
}


def add_record(user_id, date, exercise, weight, reps):
    # Generate a unique record_id (increment from the last one)
    new_id = max([record["record_id"] for record in training_data.get(user_id, [])], default=0) + 1

    # Create a new record dictionary
    new_record = {
        "record_id": new_id,
        "date": date,
        "exercise": exercise,
        "weight": weight,
        "reps": reps
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
                f"Record ID: {record['record_id']}, Date: {record['date']}, Exercise: {record['exercise']}, Weight: {record['weight']}, Reps: {record['reps']} ")
        else:
            print(f"No records found for User {user_id}")


"""
add_record(101, "2025-03-17", "Deadlift", 180, 5)
add_record(101, "2025-03-17", "sqaut", 180, 5)
add_record(102, "2025-03-17", "Deadlift", 180, 5)

formatted_users = json.dumps(training_data, indent=4)
print(formatted_users)
"""
