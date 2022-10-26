class ValidateNumber:
    def __init__(self):
        pass

    def is_number(value):
        try:
            int(value)
        except ValueError:
            return False
        return True
