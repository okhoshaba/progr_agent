# Необхідні програми для запуску 
- встановити [python3, pip3](https://www.python.org/downloads/)
- встановити [docker engine](https://docs.docker.com/engine/install/)
- встановити [docker-compose](https://docs.docker.com/compose/install/)
  
# Запуск тестового сервісу 
- Перейти в папку ```../load-testing/example-service-for-test```
- Виконати в даній папці - ```docker-compose up```
- перевірити роботоздатність сервісу

## Перевірка роботоздатності сервісу 
- відсутність помилок в конослі 
- перевірка nginx перейти за посиланням [localhost](http://localhost:8080/) результатом запиту повинна бути ```Example page !!```
- перевірка mysql використовуючи [work bench](https://www.mysql.com/products/workbench/) підключитися до бази даних: 
  - host: 127.0.0.1 
  - port: 3306
  - username: root
  - password: example

# Запуск python клієнту
- перейти в папку ```../load-testing/python-client```
- встановити необхідні пакети - виконати в даній папці ```pip3 install -r requirements.txt```  
- створити ```.env``` файл приклад налаштувань скопіювати з ```.env-example``` 
- ( за необхідністью налаштувати клієнт через ```.env```)
- Запустити ```python3 ./main.py```