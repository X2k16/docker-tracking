FROM python:3.5

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE production_settings

RUN git clone -b feat/enquete https://github.com/X2k16/tracking.git /app
ADD production_settings.py /app/src/production_settings.py

WORKDIR /app/src
RUN pip install -r /app/requirements.txt
RUN pip install gunicorn
RUN python manage.py collectstatic --noinput

VOLUME /app/static
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "tracking.wsgi:application"]

