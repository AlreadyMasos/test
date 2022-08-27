#docker + pytest + selenium
Для корректной работы необходимо установить:
- [docker desktop](https://www.docker.com/products/docker-desktop/)
- [python последней версии](https://www.python.org/downloads/)
- все необходимые зависимости языка с помощью команды: *pip install -r requirements.txt*

Далее неоходимо осуществить запуск тестовых сценариев.
Для этого есть два способа:
- напрямую через ide запустить файл test в каталоге tests
- через терминал: cd ../tests выполнить *pytest tests.py* 