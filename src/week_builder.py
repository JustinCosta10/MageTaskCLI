import shutil

class WeekBuilder:
    def __init__(self):
        terminal_size = shutil.get_terminal_size()
        detected_terminal_width = terminal_size.columns
        week_width = (7 * round(detected_terminal_width / 7) - 50)
        self.week_number = 1
        self.COLUMN_WIDTH =              week_width // 7
        self.TIME_BAR_LENGTH =           8
        self.LENGTH_OF_DAYSTRING =       3
        self.DAYS_OF_WEEK =              ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        self.CALENDAR_TIMES = [
        "07:00", "07:30", "08:00", "08:30",   "09:00", "09:30", "10:00", "10:30","11:00", "11:30", "12:00", "12:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30","04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00"]

    def print_header(self):
        print("\n")
        header = f"Week {self.week_number}"
        print(header, end="")
        print ((" " * self.TIME_BAR_LENGTH), end="")
        padding = (" " * (self.COLUMN_WIDTH - self.LENGTH_OF_DAYSTRING))
        for day in self.DAYS_OF_WEEK:
            day = f"| {day}" + f"{padding}"
            print(day, end="")
        print("|")

    def generate_week(self):
        print(("#" * (self.TIME_BAR_LENGTH + 6)), end="")
        for _ in range(len(self.DAYS_OF_WEEK)):
            dividers = "|" + ("#" * (self.COLUMN_WIDTH + 1))
            print(dividers, end="")
        print("|")
        for times in self.CALENDAR_TIMES:
            print(f"{times} " + (" " * self.TIME_BAR_LENGTH), end="")
            for _ in range(len(self.DAYS_OF_WEEK)):
                print("|" + (" " * (self.COLUMN_WIDTH +1)), end = "")
            print("|")
