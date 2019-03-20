# our base image
FROM python:3.7

COPY face_pop.py /face_pop.py

# run the application
CMD ["python", "/face_pop.py"]