class Num:
    @staticmethod
    def is_num(num: 'Num') -> bool:
        return type(num) == int or type(num) == float or type(num) == complex
