from datetime import date
from application.salary import calculate_salary
from application.db.people import get_employees
from pypi_module import spotify_funck

if __name__ == '__main__':
    today_date = date.today()
    print(today_date)
    calculate_salary()
    get_employees()
    spotify_funck()