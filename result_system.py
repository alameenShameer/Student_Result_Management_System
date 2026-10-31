students = {
    "S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
    "S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
    "S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
    "S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
    "S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}}
}


def calculate_total(marks):
    return sum(marks.values())
# print(calculate_total(students["S101"]["marks"]))


def calculate_average(marks):
    return round(calculate_total(marks)/len(marks), 2)
# print(calculate_average(students["S101"]["marks"]))


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"
# print(get_grade(calculate_average(students["S102"]["marks"])))


def check_result(marks, pass_mark=40):
    flag = 0
    for mark in marks.values():
        if mark < pass_mark:
            flag = 1
    if flag == 0:
        return "Pass"
    else:
        return "Fail"
# print(check_result(students["S102"]["marks"]))


def student_summary(student):
    summary = {}
    summary["name"] = student["name"]
    summary["total"] = calculate_total(student["marks"])
    summary["average"] = calculate_average(student["marks"])
    summary["grade"] = get_grade(summary["average"])
    summary["result"] = check_result(student["marks"])
    return summary
# print(student_summary(students["S102"]))


def add_student(data, student_id, name, **marks):
    # print(data.setdefault(student_id,{"name":name,"marks":marks}))
    if student_id in data:
        return False
    else:
        data.setdefault(student_id, {"name": name, "marks": marks})
        return True
# print(students)
# print(add_student(students,"S101","Suhail",**{"Python": 72, "Maths": 65, "Stats": 80}))
# print(students)


def update_marks(data, student_id, **changes):
    if student_id not in data:
        return "False"
    # print(data[student_id]["marks"])
    data[student_id]["marks"].update(changes)
    # print(data[student_id]["marks"])
    return "True"
# update_marks(students,"S101",**{"Maths":55})


def remove_student(data, student_id):
    if student_id in data:
        data.pop(student_id)
        return True
    else:
        return False
# print(remove_student(students,"S101"))


def print_report(data):
    average_list = []
    for id in data:
        average_list.append((calculate_average(data[id]["marks"]), id))
    average_list.sort(reverse="True")
    # print(average_list)
    print(f"{"ID":<6}{"Name":<8}{"Total":>6}{"Avg":>8}{"Grade":>7}  {"Result":<}")
    print("-"*42)
    for val in average_list:
        print(f"{val[1]:<6}{data[val[1]]["name"]:<8}{calculate_total(data[val[1]]["marks"]):>6}{calculate_average(data[val[1]]["marks"]):>8}{get_grade(calculate_average(data[val[1]]["marks"])):>7}  {check_result(data[val[1]]["marks"]):<}")


# print_report(students)


def class_statistics(data, *subjects):
    average_list = []
    for id in data:
        average_list.append((calculate_average(data[id]["marks"]), id))
    average_list.sort(reverse="True")
    print(f"Topper: {data[average_list[0][1]]["name"]}")
    pass_count = 0
    for val in data.values():
        if check_result(val["marks"])=="Pass":
            pass_count += 1
    # print(pass_count)
    total_student = len(data)
    pass_percentage = round((pass_count/total_student)*100, 1)
    print("Pass Percentage:", pass_percentage)
    total_sub = {}
    count_sub = {}
    # for sub in subjects:
    #     average=0
    for val in data.values():
        for subject, mark in val["marks"].items():
            if subject in subjects or not subjects:
                total_sub.setdefault(subject, 0)
                count_sub.setdefault(subject, 0)

                total_sub[subject] += mark
                count_sub[subject] += 1

    average_sub = {}
    for sub in total_sub:
        average_sub[sub] = round(total_sub[sub]/count_sub[sub], 2)
    print(average_sub)


# class_statistics(students, *["Python", "Maths"])

def main():
    print("Task 1 : One student")
    print(student_summary(students["S101"]))
    print(check_result(students["S102"]["marks"]))
    print(check_result(students["S102"]["marks"], 35))
    print(check_result(students["S102"]["marks"], pass_mark=35))

    print("\nTask 2 : Report")
    print_report(students)

    print("\nTask 3 : Update marks")
    print(update_marks(students, "S102", **{"Maths": 55}))
    print(update_marks(students, "S999""", **{"Maths": 55}))
    print(update_marks(students, "S102", **{"Python": 50, "Stats": 58}))
    print(student_summary(students["S102"]))

    print("\nTask 4: Add student")
    print(add_student(students, "S106", "Farhan", **
          {"Python": 70, "Maths": 35, "Stats": 74}))
    print(add_student(students, "S101", "Zara", **
          {"Python": 70, "Maths": 35, "Stats": 74}))
    print(students["S106"])

    print("\nTask 5 : Remove Student")
    print(remove_student(students, "S104"))
    print(remove_student(students, "S104"))
    print(len(students))

    print("Task 6: Final report and statistics")
    print_report(students)
    class_statistics(students)


main()
