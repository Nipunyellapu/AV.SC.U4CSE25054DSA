def search_employee(emp_list, emp_id, index=0):
    if index == len(emp_list):
        return -1
    elif emp_list[index] == emp_id:
        return index
    else:
        return search_employee(emp_list, emp_id, index + 1)

employee_ids = [101, 102, 103, 104, 105]
search_id = int(input("Enter Employee ID to search: "))

position = search_employee(employee_ids, search_id)

if position != -1:
    print("Employee ID", search_id, "found at position", position)
else:
    print("Employee ID", search_id, "not found")
