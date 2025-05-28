def add_student_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Information inserted into the Database!")
    else:
        raise TypeError("The datatype format is wrong!")


add_student_data("Sourav", 20)