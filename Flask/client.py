import requests

BASE_URL = 'http://127.0.0.1:5000/'

# Примеры запросов для пользователей
def test_users():
    # Создание пользователя
    response = requests.post(BASE_URL + 'users', json={
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'password123'
    })
    print(response.json())

    # Получение всех пользователей
    response = requests.get(BASE_URL + 'users')
    print(response.json())

    # Обновление пользователя
    user_id = 1  # Предполагая, что ID пользователя 1
    response = requests.put(BASE_URL + f'users/{user_id}', json={
        'first_name': 'Jane',
        'last_name': 'Doe',
        'email': 'jane.doe@example.com',
        'password': 'newpassword'
    })
    print(response.json())

    # Удаление пользователя
    response = requests.delete(BASE_URL + f'users/{user_id}')
    print(response.json())

# Примеры запросов для новостей
def test_news():
    # Создание новости
    response = requests.post(BASE_URL + 'news', json={
        'title': 'New Title',
        'content': 'Content of the news',
        'user_id': 1  # Предполагая, что пользователь с ID 1 существует
    })
    print(response.json())

    # Получение всех новостей
    response = requests.get(BASE_URL + 'news')
    print(response.json())

    # Обновление новости
    news_id = 1  # Предполагая, что ID новости 1
    response = requests.put(BASE_URL + f'news/{news_id}', json={
        'title': 'Updated Title',
        'content': 'Updated content'
    })
    print(response.json())

    # Удаление новости
    response = requests.delete(BASE_URL + f'news/{news_id}')
    print(response.json())

if __name__ == '__main__':
    test_users()
    test_news()
