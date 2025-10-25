student_data = []

def add_students(name, score):
    student = {"name": name, "score": score}
    student_data.append(student)
    print(f"{name} oyutniig amjilttai nemj chadsaan")

def average_score():
    if not student_data:
        print("aldaa garlaa")
        return
    niit = 0
    for student in student_data:
        niit += student["score"]
    average = niit / len(student_data)
    print(f"dundaj onoo ni {average:.2f}")


def show_status():
    if not add_students:
        print("don't have information")
        return    
    for student in student_data:
        name = student["name"]
        score = student["score"]
        status = "tentssen" if score >= 60 else "tentseegui"
        print(name, "suragltsagch", score , "onootoigoor", status)

add_students("batbold", 50)
add_students("batgerel", 100)
add_students("hangaihuu", 70)

average_score()
show_status()