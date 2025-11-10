import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "ID": [101,102,103,104,105,106,107,108,109,110],
    "Name": ["Harsh","Raj","Aman","Kunal","Abhishek","Vinay","Laksh","Yash","Rishabh","Jeswin"],
    "Maths": [85,78,92,88,65,45,67,74,91,99],
    "English": [95,74,52,98,95,95,97,84,81,89],
    "Science": [95,92,86,68,85,86,95,79,86,91],
    "Attendance": [91,88,78,65,94,88,61,87,45,77]
}

df = pd.DataFrame(data)

df['Total'] = df[['Maths', 'English', 'Science']].sum(axis=1)
df['Average'] = np.round(df['Total'] / 3, 2)

def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'E'

df['Grade'] = df['Average'].apply(get_grade)

def display_all():
    print("\n================== STUDENTS ==================")
    print(df)

def search_by_ID():
    sid = int(input("Enter the ID: "))
    student = df[df['ID'] == sid]
    if not student.empty:
        print(student)
    else:
        print("Student not found!")

def View_Stats():
    print("\n=============== CLASS STATISTICS ====================")
    print(df.describe())

def student_comparison():
    subjects = ['Maths', 'Science', 'English']
    df.plot(x='Name', y=subjects, kind='bar', figsize=(8,5))
    plt.title('Name-wise Student Performance')
    plt.xlabel('Student Name')
    plt.ylabel('Marks')
    plt.legend(title='Subjects')
    plt.tight_layout()
    plt.show()

def grade_distribution():
    df['Grade'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title("Grade Distribution")
    plt.ylabel("")  
    plt.show()

def attendanceVSperformance():
    plt.scatter(df["Attendance"], df["Average"], c=df["Average"], cmap='viridis', edgecolors='k')
    plt.title("Attendance Vs Performance")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Marks")
    plt.colorbar(label='Average Score')
    plt.grid(True, alpha=0.3)
    plt.show()

def add_new_student():
    global df  
    sid = int(input("Enter the ID: "))
    name = input("Enter the name: ")
    maths = int(input("Enter Maths Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))
    attendance = int(input("Enter Attendance (%): "))

    total = maths + science + english
    avg = round(total / 3, 2)
    grade = get_grade(avg)

    new_row = pd.DataFrame([{
        'ID': sid, 'Name': name, 'Maths': maths,
        'Science': science, 'English': english,
        'Attendance': attendance, 'Total': total,
        'Average': avg, 'Grade': grade
    }])

    df = pd.concat([df, new_row], ignore_index=True)
    print(f"\nStudent {name} added successfully!\n")


while True:
    print("\n===========================================================================")
    print("               STUDENT PERFORMANCE PORTAL                   ")
    print("===========================================================================")
    print("""
          1. Display All Students
          2. Search Student By ID
          3. View Statistics
          4. Student Performance Chart
          5. Grade Distribution
          6. Attendance VS Performance
          7. Add New Student
          8. Exit
    """)
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        display_all()
    elif choice == "2":
        search_by_ID()
    elif choice == "3":
        View_Stats()
    elif choice == "4":
        student_comparison()
    elif choice == "5":
        grade_distribution()
    elif choice == "6":
        attendanceVSperformance()
    elif choice == "7":
        add_new_student()
    elif choice == "8":
        print("Exiting Portal... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter between 1-8.")
