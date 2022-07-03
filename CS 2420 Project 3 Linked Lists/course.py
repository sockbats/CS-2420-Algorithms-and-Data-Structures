class Course:
    def __init__(self, _number=0, _name="", _credit_hr=0.0, _grade=0.0):
        try:
            _number = int(_number)
            _credit_hr = float(_credit_hr)
            _grade = float(_grade)
        except AttributeError:
            raise ValueError from AttributeError
        if type(_name) != str or _number < 0 or not 0.0 <= _grade <= 4.0 \
                or not 0.0 <= _credit_hr:
            raise ValueError from AttributeError
        self._number = _number
        self._name = _name
        self._credit_hr = _credit_hr
        self._grade = _grade
        self.next = None

    def number(self):
        """Getter for class number"""
        return self._number

    def name(self):
        """Getter for class name"""
        return self._name

    def grade(self):
        """Getter for class grade"""
        return self._grade

    def credit_hr(self):
        """Getter for class credit hour"""
        return self._credit_hr

    def __str__(self):
        return f"{self._number} {self._name} Grade: {self._grade} Credit Hours: {self._credit_hr}"
