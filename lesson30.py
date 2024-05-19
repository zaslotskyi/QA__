from datetime import datetime, timedelta


def lecture_days(start_date: str,
                 count_of_lectures: int,
                 first_day_of_week: str,
                 second_day_of_week: str,
                 start_time: str) -> str:
    """

    :param start_date: the start date of the first lecture. format '%d.%m.%Y'
    :param count_of_lectures: total number of lectures
    :param first_day_of_week: the day of the first lecture
    :param second_day_of_week: the day of the second lecture
    :param start_time: the start time of the lecture. format "%H:%M"
    :return: list of all lectures

    This function will only work if we are sure that there will be only 2 classes per week in the course.
    start_date and first_day_of_week must be specified correctly, according to the calendar, for proper calculation.
    """

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    day1 = days_of_week.index(first_day_of_week)
    day2 = days_of_week.index(second_day_of_week)

    difference_for_first_delta = (day2 - day1) % 7
    difference_for_second_delta = (day1 - day2) % 7

    list_of_lectures = list(range(1, count_of_lectures + 1))

    parsed_date = datetime.strptime(start_date, '%d.%m.%Y')
    new_date = parsed_date.strftime('%d %b')

    lectures = []

    for lecture in list_of_lectures:
        if lecture == 1:
            lectures.append(f'Lecture {lecture}: {new_date} {datetime.now().year} {start_time}')
        elif lecture % 2 == 0:
            delta = timedelta(days=difference_for_first_delta)
            date_for_pair_lectures = parsed_date + delta
            parsed_date_for_pair_lectures = date_for_pair_lectures.strftime('%d %b')
            parsed_date = date_for_pair_lectures
            lectures.append(f'Lecture {lecture}: {parsed_date_for_pair_lectures} {datetime.now().year} {start_time}')
        elif lecture % 2 != 0:
            delta = timedelta(days=difference_for_second_delta)
            date_for_odd_lectures = parsed_date + delta
            parsed_date_for_odd_lectures = date_for_odd_lectures.strftime('%d %b')
            parsed_date = date_for_odd_lectures
            lectures.append(f'Lecture {lecture}: {parsed_date_for_odd_lectures} {datetime.now().year} {start_time}')

    return '\n'.join(lectures)



print(lecture_days('11.04.2024',
                   32,
                   'Thursday',
                   'Monday',
                   '19:15'))






