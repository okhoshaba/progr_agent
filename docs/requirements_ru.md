# Постановка задачи на разработку программного агента

Целью проекта по разработке программного агента является исследование и мониторинг работы серверной части веб- (или других) сервисов корпоративной компьютерной сети на нагрузочные воздействия сторонних или разработанных программных инструментов.

1. Основные требования к архитектуре.
1.1. Архитектура программного средства состоит из серверной части (сервиса) и клиентской. 
1.2. Серверная часть (сервис) может быть реализован стандартным способом (к примеру, с помощью контейнеров с apache или nginx, с использованием различных операционных систем) или написан на языках высокого уровня Python или Java со встроенным программным агентом.
1.3. Серверная часть, которая разрабатывается на языках высокого уровня с вышеперечисленными языками программирования может содержать конфигурационный файл. 
1.4. Клиентская часть (сервис) может быть представлен стандартным инструментом (к примеру, curl или написан на языках высокого уровня Python или Java.
1.5. Клиентская часть, которая разрабатывается на языках высокого уровня с вышеперечисленными языками программирования может содержать конфигурационный файл. 
1.6. Клиентская часть может быть представлена инструментом нагрузочного воздействия (к примеру httperf), фреймворком (к примеру taurus) или скриптовым файлом (написанным, к примеру на bash). 

2. Требования к работе с серверной частью (на которой отстуствует программный агент).
2.1. Для начала работы с серверной части (на которой отстуствует программный агент) должно быть ясное описание по установке и взаимодействию с клиентской частью. При этом, должна быть указана операционная система и необходимые сведения для работы клиентов с серверной частью.
2.2. Также, могут быть указаны примеры работы клиентов с серверной частью.

3. Требования к работе клиентской части с сервисом, на котором отстуствует программный агент.
3.1. Для начала работы клиентской части с сервисом, на котором отстуствует программный агент должно быть ясное описание по установке и дальнейшей работе. При этом, должна быть указана операционная система и необходимые дополнительные сведения.
3.2. Также, могут быть указаны примеры работы клиентов с серверной частью.

4. Требования к серверной части (на которой находится программный агент).
4.1. Во время начальной загрузки серверной части (на которой находится программный агент) необходимо выполнить чтение основных параметров работы, которые находятся в конфигурационном файле. 
4.2. Структура конфигурационного файла серверной части должна состоять из записей "ключ-значение". Примеры таких записей "ключ-значение" конфигурационного файла приводятся ниже.
4.3. Клиентская часть должна иметь возможность переопределять некоторые параметры  работы серверной части с помощью запросов, которые к ней приходят. Требования к основным параметрам запросов приводятся ниже.
4.4. Все запросы к серверной части (на которой находится программный агент) от клиента делятся на команды и строки, состоящие из случайных последовательностей символов, основные параметры которых должны оговариваться и находится в конфигурационном файле.
4.5. В результате приема случайных последовательностей символов должно быть возвращена данная последовательность размером не более 250 символов.
4.6. В результате приема команды должно быть выполнена ее обработка и возвращено "ok" в случае успешного выполнения и "error" - в случае ошибки.
Пример:
from 3 to 5 - возвращается "ok", далее выполняются операции задержки последующих запросов равнораспределенным случайным образом от 3 до 5 миллисекунд.
from 5 to 3 - возвращается "error", так как 5 больше 3.
from 5 to 5 - возвращается "ok", далее выполняются операции задержки последующих запросов в 5 миллисекунд.

5. Основные требования к программному агенту.
5.1. К основным функциям тестового агента относится мониторинг работы серверной части сервиса и выполнение временных задержек на запросы пользователей.
5.2. Язык программирования Python 3, Java.
5.3. Программный агент может быть разработан с помощью языков программирования (пункт 4.2) и находится в структуре http сервиса.
 
6. Требования к конфигурационному файлу.
6.1. Конфигурационный файл должен иметь структуру "ключ-значение", которая содержит следующие ключи и их значения. Все параметры работы программного агента делятся на изменяемые и не изменяемые с помощью внешних запросов, которые направляются от клиентов.
6.2. from N. (целое значение, обозначает миллисекунды, изменяемый параметр).
6.3. to N. (целое значение, обозначает миллисекунды, изменяемый параметр).
Пример:
from 3
to 5
Выполняется операция задержки результата выполнения запроса случайным образом с помощью датчика случайных чисел (равномерное распределение) в диапазоне от 3 до 5 миллисекунд.
Если значение команд from и to совпадает - то необходимо выполнять значение задержки указанного времени.
6.4. ip N.N.N.N (IP адрес программного агента значение разделенное точками, не изменяемый параметр).
6.5. port N (номер порта программного агента (целочисленное значение, не изменяемый параметр).
Пример:
ip 192.168.222.27
port 9000
6.6. logfile str (имя лог-файла, строковое значение, может содержать цифры и знаки, изменяемый параметр).
Пример:
logfile logfile02122022.txt
6.7. log yes/no или y/n (возможность осуществлять логирование операций, бинарное значение, изменяемый параметр).
P.S. В данный раздел необходимо еще добавить параметры синхронности и асинхронности запросов.


====================================================================
P.S. Ссылка на будущие разработки в области управления трафиком:
https://apmonitor.com/pdc/index.php/Main/ArduinoTemperatureControl

