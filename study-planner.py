from datetime import datetime, timedelta

# Get subjects from user
subjects_input = input("Enter subjects (comma separated): ")
subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]

# Check if subjects entered
if not subjects:
    print("❌ Please enter at least one subject.")
    exit()

# Get exam date
exam_date_input = input("Enter exam date (YYYY-MM-DD): ")

# Validate date
try:
    exam_date = datetime.strptime(exam_date_input, "%Y-%m-%d")
except ValueError:
    print("❌ Invalid date format! Use YYYY-MM-DD")
    exit()

# Get today's date (only date, no time)
today = datetime.now().date()
exam_date = exam_date.date()

# Calculate days left
days_left = (exam_date - today).days

if days_left <= 0:
    print("❌ Exam date must be in the future!")
    exit()

# Generate study plan
print("\n📅 Your Study Plan:\n")

for i in range(days_left):
    day = today + timedelta(days=i)
    subject = subjects[i % len(subjects)]
    
    print(f"{day} → Study: {subject}")

