from course import Course
from courselist import CourseList


def main():
    with open("data.txt", "r") as f:
        data = [x.strip().split(",") for x in f.read().split("\n")]
    courses = CourseList()
    for i in data:
        courses.insert(Course(i[0], i[1], i[2], i[3]))
    print(courses)
    print(f"\n\nCumulative GPA: {courses.calculate_gpa():.3f}")


if __name__ == '__main__':
    main()
