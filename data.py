from country_list import countries_for_language
from phonenumbers.phonenumberutil import country_code_for_region

ru_surnames = [
    'Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 
    'Соколов', 'Михайлов', 'Новиков', 'Федоров', 'Морозов', 'Волков', 
    'Алексеев', 'Лебедев',
]
ru_names = [
    'Мария', 'Анастасия', 'Анна', 'Софья', 'Виктория', 'Алиса', 
    'Дарья', 'Елизавета', 'Арина', 'Полина', 'Александр', 'Даниил', 
    'Максим', 'Михаил', 'Дмитрий', 'Иван', 'Матвей', 'Роман', 'Егор', 
    'Кирилл',
]
ru_middle_names = [
    "Вячеславович", "Геннадиевич", "Георгиевич", "Григорьевич", 
    "Александрович", "Анатольевич", "Андреевич", "Игнатьевич", 
    "Игоревич", "Ильич", "Исаакович", "Феликсович", "Филиппович", 
    "Эдуардович", "Юрьевич", "Яковлевич", "Ярославович",
]
ru_cities = [
    "Екатеринбург", "Казань", "Севастополь", "Воронеж", "Псков", 
    "Красноярск", "Белгород", "Выборг", "Хабаровск", "Оренбург", 
    "Москва", "Санкт-Петербург"
]
ru_streets = [
    'Центральная', "Молодежная", "Школьная", 'Лесная', "Советская", 
    "Новая", 'Садовая', 'Набережная', 'Заречная', 'Зеленая',
]
ru_source = [
    'объявление в газете', "подруга рассказала", "реклама в метро", 
    "друг посоветовал", "таргетинг в интернете",
]


en_surnames = [
    'Smith', 'Murphy', 'Jones', 'OKelly', 'Johnson', 'Williams', 'Evans',
    'OSullivan', 'Brown', 'Walsh', 'Taylor', 'Roberts', 'ONeill', 'Wilson',
]
en_names = [
    'Oliver', 'Jack', 'Jacob', 'Noah', 'Muhammad', 'Thomas', 'Oscar', 'Layla',
    'William', 'James', 'Leo', 'Ethan', 'Isaac', 'Alexander', 'Joseph', 
    'Edward', 'Samuel', 'Max', 'Daniel', 'Arthur', 'Lucas', 'Emma', 'Olivia', 
    'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Emily', 
    'Avery', 'Sofia', 'Ella', 'Victoria', 'Aria', 'Grace', 'Chloe', 'Camila', 
    'Penelope', 'Riley', 
]
en_cities = [
    'London', 'Edinburgh', 'Manchester', 'Birmingham', 'York', 
    'Glasgow', 'Liverpool', 'Bristol', 'Oxford', 'Cambridge', 'Orlando', 
    'Los Angeles', 'Las Vegas', 'Miami', 'New York City',
]
en_streets = [
    'Oxford Street', 'Abbey Road', 'Royal Mile', 'Princes Street', 
    'Brick Lane', 'Carnaby Street', 'Piccadilly', 'Shaftesbury Avenue', 
    'The Shambles', 'Wall Street', 'Broadway', 'Bourbon Street', 
    'Hollywood Boulevard', 'Las Vegas Boulevard',  
]
en_source = [
    'heard from a friend', 'post of a blogger', 'ad in magazine',
    'advertisement on TV',
]


email_seps = ['', '-', '.', '_']
calling_code = {
    61: 'Australia', 1: 'USA', 7: 'Россия', 44: 'UK', 
    353: 'Ireland', 
}
domens = ['@mail', '@inbox', '@list', '@bk',]
languages = ['English', 'Russian']
translit = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'cz', 'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 
    'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya',
}
