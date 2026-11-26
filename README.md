# Журнал заметок

Приложение на Flask хранит заметки в SQLite. Docker Compose монтирует именованный том `arina-vis-04_notes_data` в `/data`. База находится в `/data/notes.sqlite3`.

```sh
docker compose up --build -d
```

Откройте `http://127.0.0.1:8404`, добавьте заметку и пересоздайте контейнер командой `docker compose up -d --force-recreate`. Заметка останется в списке. `docker compose down` останавливает проект и сохраняет том.

## Публикация кода

Для задания нужен репозиторий GitHub, содержащий в корне `Dockerfile`, `compose.yaml`, `requirements.txt`, `app.py` и `templates/`. Файл базы и содержимое Docker volume в репозиторий не входят. После отправки файлов укажите в работе URL репозитория.
