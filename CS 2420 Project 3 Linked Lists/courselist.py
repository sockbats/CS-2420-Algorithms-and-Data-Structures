class CourseList:
    def __init__(self):
        self.head = None

    def insert(self, course):
        if self.head is None:
            self.head = course
        elif course.number() < self.head.number():
            course.next = self.head
            self.head = course
        else:
            prev = self.head
            index = self.head.next
            if index is None:
                prev.next = course
                return
            while index is not None:
                if prev.number() <= course.number() < index.number():
                    prev.next = course
                    course.next = index
                    return
                prev = prev.next
                index = index.next
            prev.next = course

    def remove(self, number):
        index = self.head
        if index.number() == number:
            self.head = index.next
            return
        while index.next is not None:
            if index.next.number() == number:
                index.next = index.next.next
                return
            index = index.next

    def remove_all(self, number):
        index = self.head
        while index.next is not None:
            if index.number() == number:
                self.head = index.next
                return
            while index.next is not None:
                if index.next.number() == number:
                    index.next = index.next.next
                    index = self.head
                    break
                index = index.next

    def find(self, number):
        index = self.head
        i = 0
        while index.next is not None:
            if index.next.number() == number:
                return index.next
            index = index.next
            i += 1
        return -1

    def size(self):
        if self.head is None:
            return 0
        index = self.head
        i = 0
        while index.next is not None:
            index = index.next
            i += 1
        return i + 1

    def calculate_gpa(self):
        if self.head is None:
            return 0.0
        index = self.head
        i = 0
        gpa = 0
        while index.next is not None:
            gpa += index.grade() * index.credit_hr()
            i += index.credit_hr()
            index = index.next
        gpa += index.grade() * index.credit_hr()
        i += index.credit_hr()
        return gpa / i

    def is_sorted(self):
        if self.head is None:
            return True
        index = self.head
        while index.next is not None:
            if not index.number() <= index.next.number():
                return False
            index = index.next
        return True

    def __str__(self):
        course_list = ""
        index = self.head
        while index.next is not None:
            course_list += f"{index}\n"
            index = index.next
        course_list += f"{index}"
        return course_list

    def __iter__(self):
        self.index = self.head
        return self

    def __next__(self):
        if self.index is None:
            raise StopIteration
        current = self.index
        self.index = self.index.next
        return current
