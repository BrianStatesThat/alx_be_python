# Get task details from user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match case
match priority:
    case "high":
        priority_msg = "high priority task"
    case "medium":
        priority_msg = "medium priority task"
    case "low":
        priority_msg = "low priority task"
    case _:
        priority_msg = "task with unspecified priority"

# Create reminder based on time sensitivity
if time_bound == "yes":
    reminder = f"Reminder: '{task}' is a {priority_msg} that requires immediate attention today!"
else:
    reminder = f"Note: '{task}' is a {priority_msg}. Consider completing it when you have free time."

# Print the reminder
print("\n" + reminder)