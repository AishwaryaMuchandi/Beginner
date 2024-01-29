# Write a program to construct a dictionary from the two lists
# containing the names of students and their corresponding
# subjects. The dictionary should map the students with their
# respective subjects. Let’s see how to do this using for loops and
# dictionary comprehension.
# Input: [Sam, Alice, Mona] ,
# [Commerce, Science, Computer]
# Output: [Sam: Commerce, Alice: Science , Mona: Computer]

def create_student_subject_dict(students, subjects):
    student_subject_dict = {students[i]: subjects[i] for i in range(len(students))}
    return student_subject_dict

def create_student_subject_dict_with_loop(students, subjects):
    student_subject_dict = {}
    for i in range(len(students)):
        student_subject_dict[students[i]] = subjects[i]
    return student_subject_dict

students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

student_subject_dict = create_student_subject_dict(students, subjects)

student_subject_dict_with_loop = create_student_subject_dict_with_loop(students, subjects)

print("Output using dictionary comprehension:", student_subject_dict)
print("Output using for loop:", student_subject_dict_with_loop)
