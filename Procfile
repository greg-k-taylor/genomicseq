web: gunicorn genomicseq.wsgi -w 3
celery: python manage.py celeryd -E -l info -c 3 --beat
clock: python clock.py
