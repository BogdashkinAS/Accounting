from datetime import *
from application.salary import *
from application.db.people import *
from pypi_module import *

if __name__ == '__main__':
    today_date = date.today()
    print(today_date)
    calculate_salary()
    get_employees()
    spotify_funck()