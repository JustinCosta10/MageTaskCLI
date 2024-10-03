class ConvertRegToMil:
    def __init__(self, time_input: str):
        self.time_input = time_input
        self.time_value = None
        self.time_sanitized = None
        self.a_p = None

    def sanitize_time_input(self):
        if (len(self.time_input) == 4) or (len(self.time_input) == 5):
            if self.time_input[-1] == 'a':
                self.time_sanitized = self.time_input.split('a')
                self.time_string = self.time_sanitized[0]
                self.time_value = int(self.time_sanitized[0])
                self.a_p = 'a'
                print(self.time_value)

            elif self.time_input[-1] == 'p':
                self.time_input.split('p')
                self.time_sanitized = self.time_input.split('p')
                self.time_value = int(self.time_sanitized[0])
                self.a_p = 'p'
                print(self.time_value)
            else:
                return
    def __split_time_int(self):
        split_time = self.time_value
        hours = split_time // 100
        minutes = split_time % 100
        return hours, minutes

    def __is_valid_time(self):
        if self.time_value is None:
            return False
        if not (100 <= self.time_value <= 1259):
            return False

        hours, minutes = self.__split_time_int()

        if 1 <= hours <= 12 and 0 <= minutes <= 59:
            return True
        else:
            return False

    def convert_12_24(self): #in format 530a / 1230p
        if not self.__is_valid_time():
            print ("Enter a valid time. Ex: (230a 1030 530p 1130p)")
            return None
        time = self.time_value
        if self.a_p == 'a':
            if time == 1200:
                time = 0
            return time

        elif self.a_p == 'p':
            if (time < 1200):
                time += 1200
            return time

    def reg_to_mil_convert(self):
        time = ConvertRegToMil(self.time_input)
        time.sanitize_time_input()
        military_time = time.convert_12_24()
        return military_time


class ConvertMilToReg:
    def __init__(self, time_input: int):
        self.time_input = time_input

    def __split_time_int(self):
        split_time = self.time_input
        hours = split_time // 100
        minutes = split_time % 100
        return hours, minutes

    def __is_valid_time(self):
        if not (0 <= self.time_input <= 2359):
            return False

        hours, minutes = self.__split_time_int()

        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return True
        else:
            return False
    def convert_24_12(self): #in format 1130 / 1430
        if not self.__is_valid_time():
            print ("Enter a valid time. Ex: (230a 1030 530p 1130p)")
            return None
        time = self.time_input
        if time == 0 or time == 2400:
            return "1200a"
        elif time < 1200:
            return f"{time}a"
        elif time == 1200:
           return f"{time}p"
        else:
            time -= 1200
            return f"{time}p"

    def mil_to_reg_convert(self):
        time = ConvertMilToReg(self.time_input)
        return time.convert_24_12()
