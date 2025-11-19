import json
import http.client
from urllib.parse import urlparse


# ASGI/WSGI функция
def application(environ, start_response):
    # Получаем путь запроса
    path = environ.get('PATH_INFO', '/')

    # Извлекаем валюту из пути
    currency = path.strip('/').upper()

    if not currency:
        # Если валюта не указана, возвращаем ошибку 400
        status = '400 Bad Request'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)
        return [b'{"error": "Currency not specified"}']

    # Формируем запрос к стороннему API
    conn = http.client.HTTPSConnection("api.exchangerate-api.com")

    try:
        conn.request("GET", f"/v4/latest/{currency}")
        response = conn.getresponse()

        # Читаем данные ответа
        data = response.read()

        if response.status == 200:
            # Успешный ответ, возвращаем данные
            status = '200 OK'
            headers = [('Content-Type', 'application/json')]
            start_response(status, headers)
            return [data]
        else:
            # Если произошла ошибка, возвращаем статус и сообщение
            status = f'{response.status} {response.reason}'
            headers = [('Content-Type', 'application/json')]
            start_response(status, headers)
            return [data]

    except Exception as e:
        # Обработка исключений
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)
        return [bytes(json.dumps({"error": str(e)}), 'utf-8')]

    finally:
        conn.close()


# Если вы хотите протестировать приложение локально с помощью WSGI сервера, используйте следующий код:
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()