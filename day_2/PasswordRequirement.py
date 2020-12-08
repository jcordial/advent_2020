class PasswordRequirement():
    lower_number: int = 0;
    higher_number: int = 0
    test_string: str = ''

    def __init__(self, required_string: str, min: int = 0, max: int = 0) -> None:
        super().__init__()
        self.lower_number = min
        self.higher_number = max
        self.test_string = required_string

    def validate(self, password: str):
        raise NotImplementedError

