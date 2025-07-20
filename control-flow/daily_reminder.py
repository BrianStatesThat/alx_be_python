# Prompt for task details
task = input("Enter your priority task for today: ")
priority = input("Enter task priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process task using match case
match priority:
    case "high":
        reminder = f"❗ High priority: {task}"
    case "medium":
        reminder = f"🔸 Medium priority: {task}"
    case "low":
        reminder = f"▫️ Low priority: {task}"
    case _:
        reminder = f"Unknown priority: {task}"

# Add time sensitivity information
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += " - no immediate deadline."

# Print the customized reminder
print("\nYour daily reminder:")
print(reminder)