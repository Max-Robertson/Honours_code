FROM python:3-onbuild
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY docker_face_pop.py /docker_face_pop.py
#RUN pip install . 
EXPOSE 27017
CMD ["python", "/docker_face_pop.py"]