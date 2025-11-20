from abc import ABC, abstractmethod
from typing import Union

class Person(ABC):

    def __init__(self, full_name: str, age: int) -> None:
        self._full_name = full_name
        self._age = age

    def print_info(self) -> None:
        print(f"ФИО: {self._full_name}, Возраст: {self._age}")

    @abstractmethod
    def get_scholarship(self) -> int:
        pass

    def print_scholarship(self) -> None:
        print(f"Размер стипендии: {self.get_scholarship()} руб.")

    def compare_scholarship(self, other: 'Person') -> str:
        scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()

        if scholarship > other_scholarship:
            return "больше"
        elif scholarship < other_scholarship:
            return "меньше"
        return "равна"

class Student(Person):

    EXCELLENT_SCHOLARSHIP = 6000
    STANDARD_SCHOLARSHIP = 4000
    NO_SCHOLARSHIP = 0
    EXCELLENT_THRESHOLD = 5
    STANDARD_THRESHOLD = 4

    def __init__(self,
                 full_name: str,
                 age: int,
                 group: str,
                 average_score: float
                 ) -> None:
        pass
        super().__init__(full_name, age)
        self._group = group
        self._average_score = average_score

    def get_scholarship(self) -> int:
        if self._average_score >= self.EXCELLENT_THRESHOLD:
            return self.EXCELLENT_SCHOLARSHIP
        elif self._average_score >= self.STANDARD_THRESHOLD:
            return self.STANDARD_SCHOLARSHIP
        return self.NO_SCHOLARSHIP


class GraduateStudent(Person):

    EXCELLENT_SCHOLARSHIP = 8000
    STANDARD_SCHOLARSHIP = 6000
    NO_SCHOLARSHIP = 0
    EXCELLENT_THRESHOLD = 5
    STANDARD_THRESHOLD = 4

    def __init__(self, full_name: str, age: int, group: str,
                 average_score: float, research_topic: str) -> None:
        super().__init__(full_name, age)
        self._group = group
        self._average_score = average_score
        self._research_topic = research_topic

    def get_scholarship(self) -> int:
        if self._average_score >= self.EXCELLENT_THRESHOLD:
            return self.EXCELLENT_SCHOLARSHIP
        elif self._average_score >= self.STANDARD_THRESHOLD:
            return self.STANDARD_SCHOLARSHIP
        return self.NO_SCHOLARSHIP

if __name__ == "__main__":
    student = Student("Владимир Владимирович Калашников", 20,
                      "Группа 5132704/30801", 4.5)
    graduate = GraduateStudent("Зубков Тимофей Сергеевич", 25,
                               "Группа 5132704/10801", 5.0,
                               "Алгоритм стыковки космических "
                               "аппаратов на основе нечеткой логики")

    print("Информация о студенте:")
    student.print_info()
    student.print_scholarship()

    print("\nИнформация об аспиранте:")
    graduate.print_info()
    graduate.print_scholarship()

    print(f"\nСтипендия студента {student.compare_scholarship(graduate)} "
         "стипендии аспиранта")
