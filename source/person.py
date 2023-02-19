"""Генерация персональных данных лица"""

from faker import Faker
from faker.providers import DynamicProvider
from random import randint, choice, gauss
from scipy import stats as sts
from datetime import datetime
from dateutil.relativedelta import relativedelta

fake = Faker("ru_RU")

def get_loan() -> str | None:
    """Возвращает случайный банк или None"""

    loan = fake.bank()
    return choice([None, loan])

def get_loan_size() -> float | None:
    """Возвращает размер имеющегося кредита"""

    bottom = 15000
    top = 15000000
    return randint(bottom, top)

def get_children() -> int:
    """Возвращает число детей на иждивении"""

    n_child = -1

    while n_child < 0:
        n_child = int(gauss(mu=1, sigma=1.0))
    
    return n_child 

def get_salary() -> int:
    """Возвращает размер заработной платы. Распределение Хи-квадрат."""

    chi = sts.chi2(df=3)
    salary = int(chi.rvs())*20000
    
    return salary

sex = DynamicProvider("sex", ["m", "f"])    # пол
fake.add_provider(sex)


def get_birthday() -> str:
    """Возвращает дату рождения"""

    rv = sts.norm(50, 20)
    age = rv.rvs().astype(int)
    now = datetime.now()
    birthday = datetime.now() - relativedelta(years=age)

    return birthday.strftime("%Y-%m-%d")

def get_applying() -> str:
    """Возвращает дату и время обращения заявителя"""

    now = datetime.now()
    delta = randint(-10, 10)
    appl = now - relativedelta(days=delta)

    return appl.strftime("%Y-%m-%d %H:%M")

def get_person() -> dict[str, str | int]:
    """Возвращает персональные данные лица"""

    person = { 
            "name": fake.name(),   
            "sex": fake.sex() ,
            "applying": get_applying(),
            "birthday": get_birthday(),
            "region": fake.region(),
            "job": fake.job(),
            "phone": fake.phone_number(),
            "loan": get_loan(),
            "children": get_children(),
            "residence_type": choice(list("ABCD")),
            "salary": get_salary()
    }

    if person["loan"]:
        person["loan_size"] = get_loan_size()

    else:
        person["loan_size"] = None

    return person

if __name__ == "__main__":
    person = get_person()
    print(person)
