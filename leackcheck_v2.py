import requests
import time
import argparse

API_KEY = "API_KEY"
API_URL = "https://leakcheck.io/api/v2/query"

def search_leak(query, query_type="auto"):
    """
    Поиск утечек через API v2 LeakCheck
    """
    headers = {
        "Accept": "application/json",
        "X-API-Key": API_KEY
    }
    
    # Добавляем параметры запроса
    params = {}
    if query_type != "auto":
        params["type"] = query_type

    try:
        response = requests.get(f"{API_URL}/{query}", headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"Произошла HTTP ошибка: {http_err}")
        print(f"Содержимое ответа: {response.content}")
        return None
    except requests.exceptions.SSLError as ssl_err:
        print(f"Произошла SSL ошибка: {ssl_err}")
        return None
    except Exception as err:
        print(f"Произошла ошибка: {err}")
        return None

def format_result(result):
    """
    Форматирование результатов поиска
    """
    formatted_results = []
    for item in result['result']:
        # Получаем все возможные поля из ответа API v2
        email = item.get('email', '')
        username = item.get('username', '')
        password = item.get('password', '')
        phone = item.get('phone', '')
        first_name = item.get('first_name', '')
        last_name = item.get('last_name', '')
        
        # Формируем строку результата в зависимости от наличия данных
        if email and password:
            formatted_results.append(f"{email}:{password}")
        elif email:
            formatted_results.append(email)
        elif username and password:
            formatted_results.append(f"{username}:{password}")
        elif username:
            formatted_results.append(username)
        elif phone:
            formatted_results.append(phone)
        
        # Добавляем дополнительную информацию, если она есть
        if first_name or last_name:
            additional_info = f"{first_name} {last_name}".strip()
            if additional_info:
                formatted_results[-1] += f" | {additional_info}"

    return formatted_results

def process_queries(queries, query_type, output_file):
    """
    Обработка списка запросов
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for query in queries:
            query = query.strip()
            if query:
                result = search_leak(query, query_type)
                if result and result.get('success') and result.get('found', 0) > 0:
                    formatted_results = format_result(result)
                    for formatted_result in formatted_results:
                        print(formatted_result)  # Вывод в консоль
                        outfile.write(formatted_result + "\n")
                    
                    # Выводим информацию об оставшейся квоте
                    if 'quota' in result:
                        print(f"Осталось запросов: {result['quota']}")
                else:
                    print(f"Результатов не найдено для запроса '{query}'")
                
                # Ограничение запросов (3 запроса в секунду по умолчанию)
                time.sleep(0.35)

def main(args):
    """
    Основная функция программы
    """
    queries = []
    if args.input_list:
        with open(args.input_list, 'r', encoding='utf-8') as infile:
            queries = infile.readlines()
    if args.input:
        queries.append(args.input)
    
    process_queries(queries, args.query_type, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Поиск утечек данных через LeakCheck API v2")
    parser.add_argument('-iL', '--input-list', help="Путь к файлу со списком запросов")
    parser.add_argument('-i', '--input', help="Одиночный запрос (email, domain, phone и т.д.)")
    parser.add_argument('-t', '--query-type', default="auto", 
                       help="Тип запроса (auto, email, domain, phone, username, hash, keyword и т.д.)")
    parser.add_argument('-o', '--output', required=True, 
                       help="Путь к файлу для сохранения результатов")
    
    args = parser.parse_args()

    if not args.input_list and not args.input:
        parser.error("Требуется указать хотя бы один из параметров: --input-list или --input")
    
    main(args)
