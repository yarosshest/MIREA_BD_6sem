from console.db.Collection import Collection
from schema import Schema


class Clients(Collection):
    name = "Clients"
    schema = Schema({
        "FIO": str,
        "Tel": str,
        "Email": str
    })

    def __init__(self):
        super().__init__(self.name, self.schema)

    def insertTestData(self):
        self.insert([
            {"FIO": "г-жа Ковалева Лукия Ждановна", "Tel": "8 (142) 445-86-17", "Email": "trofim1976@mail.ru"},
            {"FIO": "тов. Игнатова Наина Петровна", "Tel": "+7 (428) 328-04-67", "Email": "evseevafaina@rambler.ru"},
            {"FIO": "Варлаам Ефимович Селиверстов", "Tel": "+7 461 822 54 37", "Email": "eliseevkuprijan@hotmail.com"},
            {"FIO": "Герасим Елизарович Власов", "Tel": "+7 (278) 212-8013", "Email": "nfomichev@yandex.ru"},
            {"FIO": "Ковалев Будимир Венедиктович", "Tel": "8 (513) 761-46-22", "Email": "vishnjakovdemjan@hotmail.com"},
            {"FIO": "Панкратий Венедиктович Шарапов", "Tel": "8 188 377 4354", "Email": "filippgavrilov@hotmail.com"},
            {"FIO": "Шубин Вышеслав Теймуразович", "Tel": "+74399067629", "Email": "margarita2015@rambler.ru"},
            {"FIO": "Алла Павловна Александрова", "Tel": "8 625 428 9299", "Email": "vishnjakovvasili@yandex.ru"},
            {"FIO": "Назарова Валентина Максимовна", "Tel": "+7 (926) 211-07-10", "Email": "gerasim_1984@yahoo.com"},
            {"FIO": "Филиппов Флорентин Ильясович", "Tel": "+7 (495) 459-18-38", "Email": "vzhuravleva@rambler.ru"},
        ])
        print("Clients test data inserted")
