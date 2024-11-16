from math import ceil


class OnlineCourse:
    course_dict = dict()

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
        self.course_dict["name"] = name
        self.course_dict["description"] = description
        self.course_dict["weeks"] = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> "OnlineCourse":
        name = course_dict["name"]
        description = course_dict["description"]
        days = course_dict["days"]
        weeks = cls.days_to_weeks(days)
        return cls(name, description, weeks)
