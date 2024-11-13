import sqlite3


conn = sqlite3.connect("sample.db")


cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Student (
        StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        DateOfBirth DATE NOT NULL,
        Gender TEXT NOT NULL,
        Address TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Teacher (
        TeacherID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        DateOfBirth DATE NOT NULL,
        Gender TEXT NOT NULL,
        Address TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Parent (
        ParentID INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        Address TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Class (
        ClassID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClassName TEXT NOT NULL,
        Section TEXT NOT NULL
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Subject (
        SubjectID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClassName TEXT NOT NULL
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ClassSubMap (
        MappingID INTEGER PRIMARY KEY AUTOINCREMENT,
        ClassID INTEGER,
        SubjectID INTEGER,
        TeacherID INTEGER,
        FOREIGN KEY (ClassID) REFERENCES Class(ClassID),
        FOREIGN KEY (SubjectID) REFERENCES Subject(SubjectID),
        FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID)
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Enrollment (
        EnrollmentID INTEGER PRIMARY KEY AUTOINCREMENT,
        StudentID INTEGER,
        ClassID INTEGER,
        EnrollmentDate DATE NOT NULL,
        FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
        FOREIGN KEY (ClassID) REFERENCES Class(ClassID)
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Grade (
        GradeID INTEGER PRIMARY KEY AUTOINCREMENT,
        EnrollmentID INTEGER,
        StudentID INTEGER,
        TeacherID INTEGER,
        ExamDate DATE NOT NULL,
        Marks INTEGER NOT NULL,
        FOREIGN KEY (EnrollmentID) REFERENCES Enrollment(EnrollmentID),
        FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
        FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID)
    );
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Attendance (
        AttendanceID INTEGER PRIMARY KEY AUTOINCREMENT,
        EnrollmentID INTEGER,
        AttendanceDate DATE NOT NULL,
        Status TEXT NOT NULL,
        FOREIGN KEY (EnrollmentID) REFERENCES Enrollment(EnrollmentID)
    );
"""
)

cursor.execute("select * from Student where FirstName = 'Kushagra';")
result = cursor.fetchall()

for res in result:
    print(res)

conn.commit()
conn.close()
