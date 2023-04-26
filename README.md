# Новое русское вино
Сайт магазина авторского вина "Новое русское вино".

## Окружение
### Зависимости
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

### Переменные окружения
- WINES_EXCEL_PATH

1. Поместите файл `.env` рядом с `main.py`.
2. `.env` должен содержать текстовые данные без кавычек.

Например, если вы распечатаете содержимое `.env`, то увидите:

```bash
$ cat .env
WINES_EXCEL_PATH=wine.xlsx
```

## Запуск
Запуск на Linux(Python 3) или Windows:

```bash
$ python main.py
```
Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).