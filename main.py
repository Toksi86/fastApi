from fastapi import FastAPI

app = FastAPI(
    title='Учебный проект'
)

test_users = [
    {'id': 1, 'name': 'Vasya', 'age': 26},
    {'id': 2, 'name': 'Kolya', 'age': 32},
    {'id': 3, 'name': 'Olya', 'age': 23},
    {'id': 4, 'name': 'Nastya', 'age': 21},
]

books_read = [
    {'id': 1, 'user_id': 1, 'book_name': 'The Little Prince'},
    {'id': 2, 'user_id': 1, 'book_name': 'The Hobbit'},
    {'id': 3, 'user_id': 1, 'book_name': 'The Da Vinci Code'},
    {'id': 4, 'user_id': 3, 'book_name': 'The Alchemist '},
    {'id': 5, 'user_id': 3, 'book_name': 'The Great Gatsby'},
] 


# Создание параметра пути
# Анотация изменяет тип данных получаемого агумента
@app.get('/users/{user_id}')
def get_user(user_id: int):
    if len(test_users) >= user_id:
        return [user for user in test_users if user.get('id') == user_id]
    else:
        return 'User not found'


# Создание параметров запроса с дефлотным значением
@app.get('/books/{user_id}')
def get_reads_books(user_id: int, limit: int = 3):
    books = [book for book in books_read if book.get('user_id') == user_id]
    return [book.get('book_name') for book in books][:limit]


# Создание post запроса на существующий ендпоинт
@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    for user in test_users:
        if user['id'] == user_id:
            user['name'] = new_name
            return user
    return 'User not found'
