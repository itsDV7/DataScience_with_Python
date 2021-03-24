from random import randint

studentDB_dict = {}


class StudentDB:

    def add_student(self, name_add, number_add, department_add):
        studentDB_dict[randint(1, 1000)] = [name_add, number_add, department_add]
        print("\nStudent Added to Database!\n")
        self.show_db()

    def delete_student(self, id_del):
        try:
            del studentDB_dict[id_del]
            print("\nStudent {} Deleted from Database!\n".format(id_del))
            self.show_db()
        except KeyError:
            print("\nNo such Entry: {}".format(ID))

    @staticmethod
    def show_db():
        print("\nCurrent Database:\n")
        for k, v in studentDB_dict.items():
            print("ID: {}   Name: {}    Number: {}    Department: {}".format(k, v[0], v[1], v[2]))


if __name__ == "__main__":
    obj = StudentDB()
    while 1:
        print("\n1. Add Student\n2. Delete Student\n3. Show Database\n4. Exit\n")
        try:
            ch = int(input())
        except ValueError:
            print("\nIncorrect Input!\n")
            continue
        if ch == 1:
            name = input("Enter Name: ")
            number = input("Enter Number: ")
            department = input("Enter Department: ")
            obj.add_student(name, number, department)
            continue
        elif ch == 2:
            if len(studentDB_dict) == 0:
                print("\nDatabase is Empty!\n")
                continue
            else:
                ID = int(input("Enter Student ID: "))
                obj.delete_student(ID)
                continue
        elif ch == 3:
            if len(studentDB_dict) == 0:
                print("\nDatabase is Empty!\n")
                continue
            else:
                obj.show_db()
                continue
        elif ch == 4:
            print("\nExiting...\n")
            break
        else:
            print("\nIncorrect Input!\n")
            continue
