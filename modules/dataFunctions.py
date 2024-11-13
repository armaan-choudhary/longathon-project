import sqlite3

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()


def AddStudent(fName, lName, dob, gender, address, pNo):
    cursor.execute(
        """
      INSERT INTO Student (FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber)
      VALUES (?, ?, ?, ?, ?, ?)
    """,
        (fName, lName, dob, gender, address, pNo),
    )


def UpdateStudent(id, fName="", lName="", dob="", gender="", address="", pNo=""):
    cursor.execute("SELECT * FROM Student WHERE StudentID = ?", (id,))
    studInfo = cursor.fetchone()

    if studInfo:
        cursor.execute(
            """
            UPDATE Student
            SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Address = ?, PhoneNumber = ?
            WHERE StudentID = ?
            """,
            (
                fName or studInfo[1],
                lName or studInfo[2],
                dob or studInfo[3],
                gender or studInfo[4],
                address or studInfo[5],
                pNo or studInfo[6],
                id,
            ),
        )
    else:
        print("Student not found")


def DeleteStudent(id):
    cursor.execute("DELETE FROM Student WHERE StudentID = ?", (id,))
    print("Deleted !")


def SearchStudentByID(id):
    cursor.execute(
        "SELECT StudentID, FirstName, LastName FROM Student WHERE StudentID = ?", (id,)
    )

    rows = cursor.fetchall()
    if rows == []:
        print("No Records Found.")
    else:
        for row in rows:
            print("\nTeacher No.", row[0], "\nName :", row[1], row[2])


def SearchStudentByName(n):
    cursor.execute(
        "SELECT StudentID, FirstName, LastName FROM Student WHERE FirstName = ? OR LastName = ?",
        (
            n,
            n,
        ),
    )

    rows = cursor.fetchall()
    if rows == []:
        print("No Records Found.")
    else:
        for row in rows:
            print("\nTeacher No.", row[0], "\nName :", row[1], row[2])


def AddTeacher(fName, lName, dob, gender, address, pNo):
    cursor.execute(
        """
      INSERT INTO Teacher (FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber)
      VALUES (?, ?, ?, ?, ?, ?)
    """,
        (fName, lName, dob, gender, address, pNo),
    )


def UpdateTeacher(id, fName="", lName="", dob="", gender="", address="", pNo=""):
    cursor.execute("SELECT * FROM Teacher WHERE TeacherID = ?", (id,))
    teachInfo = cursor.fetchone()

    if teachInfo:
        cursor.execute(
            """
            UPDATE Teacher
            SET FirstName = ?, LastName = ?, DateOfBirth = ?, Gender = ?, Address = ?, PhoneNumber = ?
            WHERE StudentID = ?
            """,
            (
                fName or teachInfo[1],
                lName or teachInfo[2],
                dob or teachInfo[3],
                gender or teachInfo[4],
                address or teachInfo[5],
                pNo or teachInfo[6],
                id,
            ),
        )
    else:
        print("Student not found")


def DeleteTeacher(id):
    cursor.execute("DELETE FROM Teacher WHERE TeacherID = ?", (id,))
    print("Deleted !")


def SearchTeacherByID(id):
    cursor.execute(
        "SELECT TeacherID, FirstName, LastName FROM Teacher WHERE TeacherID = ?", (id,)
    )

    rows = cursor.fetchall()
    if rows == []:
        print("No Records Found.")
    else:
        for row in rows:
            print("\nTeacher No.", row[0], "\nName :", row[1], row[2])


def SearchTeacherByName(n):
    cursor.execute(
        "SELECT TeacherID, FirstName, LastName FROM Teacher WHERE FirstName = ? OR LastName = ?",
        (
            n,
            n,
        ),
    )

    rows = cursor.fetchall()
    if rows == []:
        print("No Records Found.")
    else:
        for row in rows:
            print("\nTeacher No.", row[0], "\nName :", row[1], row[2])


SearchTeacherByName("Dhruv")


# conn.commit()
# conn.close()
