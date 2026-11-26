FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 NOTES_DB=/data/notes.sqlite3
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && useradd --system --uid 10001 --no-create-home app \
    && mkdir /data && chown app /data
COPY app.py .
COPY templates/ templates/
USER app
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "app:app"]
