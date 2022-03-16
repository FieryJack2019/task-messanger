### Task-messanger

## Документация
# Сборка
  * Клонирование репозитория git clone https://github.com/FieryJack2019/task-messanger
  * Сборка докер образа docker-compose up -d --build

# Настройка oAuth2
1. Cоздание суперюзера
  * sudo docker-compose exec webapp bash
  * cd messanger
  * python3 manage.py createsuperuser
2. Создание Oauth2 application
  * Переходим /auth/applications/
  * Создаем новое приложение и задаем
  Client type = Confidential 
  Authorization grant type =Resource owner password-based
  * Копируем **Client id** и **Client secret**
3. Получение токена авторизации
  * Используя полученные **Client id** и **Client secret** делаем пост запрос на /auth/token

# Запуск листенера:
  * sudo docker-compose exec webapp bash
  * cd messanger
  * python3 manage.py messages_confirmation <созданный токен>
  * в админке Django добавляем необходимые слова в модель **Черный список**
