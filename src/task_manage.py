from task_db.query_service import QueryService
from time_converter.time_converter import ConvertRegToMil

class TaskManage:
    def __init__(self):
        pass

    def numbered_day(self, day):
        days = {'sun': 1, 'mon': 2, 'tue': 3, 'wed': 4, 'thu': 5, 'fri': 6, 'sat': 7}
        return days.get(day.strip().lower(), 0)

    def create_task(self, task_desc, task_day, task_time):
        if len(task_desc) > 25:
            print("Task description must be less than 25 characters.")
            return

        day_number = self.numbered_day(task_day)
        if day_number == 0:
            print("Invalid day entry. (ex. mon, tue, wed, etc...)")
            return

        task_time = ConvertRegToMil(task_time).reg_to_mil_convert()
        if not isinstance(task_time, int):
            print("Invalid time format.")
            return

        QueryService().insert_query(task_desc, day_number, task_time)

    def delete_task(self, task_desc):
        QueryService().delete_query(task_desc)

    def pull_tasks(self):
        tasks = QueryService().query_all()
        if not tasks:
            return "No tasks available."

        days_of_week = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
        sorted_tasks = sorted(tasks, key=lambda x: (x[1], x[2]))

        tasks_by_day = {day: [] for day in range(1, 8)}

        for task in sorted_tasks:
            day_name = days_of_week.get(task[1], 'Unknown')
            task_time = self._format_time(task[2])
            tasks_by_day[task[1]].append(f"{task_time} - {task[0]}")

        output = ""
        for day in range(1, 8):
            day_tasks = tasks_by_day[day]
            day_name = days_of_week[day]
            if day_tasks:
                output += f"\n{day_name}:\n" + "\n".join(day_tasks) + "\n"

        return output.strip()

    def _format_time(self, military_time):
        hour = military_time // 100
        minute = military_time % 100
        period = "AM" if hour < 12 else "PM"
        if hour > 12:
            hour -= 12
        elif hour == 0:
            hour = 12
        return f"{hour}:{minute:02d} {period}"

    def reset_tasks(self):
        QueryService().reset_all_tasks()
