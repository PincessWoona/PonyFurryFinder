# Pony/Furry image finder

Вы можете найти любую картинку используя лишь теги и магию запросов.

## Установка

```
git clone https://github.com/PincessWoona/PonyFurryFinder.git
cd PonyFurryFinder

pip install requests flask

vim app.py
```
Отредактируйте строки связанные с api:
```
DERPIBOORU_API_KEY = "**************"
FURBOORU_API_KEY = "**************"
```

Вместо звездочек должны быть ваши API-ключи, которые вы можете получить на сайтах furbooru.org и derpibooru.org.
В разделе `/registrations/edit`

## Запуск

```
python app.py

```

