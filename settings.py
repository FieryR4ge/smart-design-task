MONGO_HOST = 'localhost'  # Сервер MongoDb
MONGO_PORT = 27017  # Порт MongoDb
MONGO_DBNAME = 'Phone'  # Имя базы данных

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']  # Включение методов для ресурсов (коллекций)
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']  # Включение методов для элемента ресурса (коллекции)

X_DOMAINS = '*'  # Домены (IP), с которых разрешена работа с приложением (* - все домены)
X_HEADERS = ['Content-Type', 'Accept', 'If-Match', 'Authorization', 'Cache-Control', 'Pragma',
             'Expires']  # Разрешенные заголовки

# Описание документов
DOMAIN = {

    'goods': {
        'schema': {
            'name': {
                'type': 'string',
                'required': True,
            },
            'ID': {
                'type': 'string',
                'required': True,
                'unique': True
            },
            'description': {
                'type': 'string',
                'required': True
            }
        }
    }
}
