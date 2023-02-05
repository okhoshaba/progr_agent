# python load test serviece

Run service ( read service/README.md )
Run load-testing-service ( read load-testing-service/README.md )


# Program agent

# Start agent 

python ./src/http_service.py 

# Config agent 

Agent config from file - "./config.json"

{
    "ip": "localhost", // ip N.N.N.N (IP адрес программного агента значение разделенное точками, не изменяемый параметр)
    "port": 9000, // port N (номер порта программного агента (целочисленное значение, не изменяемый параметр).
    "from": 10, // default lowest delay 
    "to": 100,  // default highest delay 
    "logfile": "test.log", // имя лог-файла, строковое значение, может содержать цифры и знаки, изменяемый параметр.
    "log": true // true/false возможность осуществлять логирование операций, бинарное значение, изменяемый параметр
}

# Testing agent

Run python ./src/test.py 

messageList - list of message that send in same time for strest test agent
