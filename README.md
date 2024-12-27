## Запуск контейнеров

#### Пример .evn файла
```
ETU_ID_LOGIN=login
ETU_ID_PASSWORD=password
WEB_SERVER_PORT=5000
```

### Сборка образов
```shell
docker compose build
```

### Запуск контейнеров
```shell
docker compose up
```

### app контейнер

#### Внешний SSH доступ в контейнер
```shell
ssh -i ssh/authorized_keys/docker_rsa -p 2222 root@127.0.0.1
```

### tester контейнер

#### Запуск всех этапов тестирования
```shell
docker compose exec tester tests/run.sh --all
```

#### Проверка на соответствие стилю кодирования (black)
```shell
docker compose exec tester tests/run.sh --test code_style
```

#### Линтинг (pylint)
```shell
docker compose exec tester tests/run.sh --test linting
```

#### Selenium-тесты
```shell
docker compose exec tester tests/run.sh --test selenium
```

#### Интеграционные тесты
```shell
docker compose exec tester tests/run.sh --test integration
```

