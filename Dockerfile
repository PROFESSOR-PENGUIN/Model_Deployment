FROM python:3.9
#working directory of container
WORKDIR /app
#copy current workdir to app directory in container
COPY . /app
#install requirements
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#expose a port for container to run
EXPOSE 8000
#write execution command for docker terminal, if keywords separated by space write them in separate quotes
#CMD ["python3","api.py"]
#the host in CMD is used by container 0.0.0.0 is for localhost in container
CMD ["uvicorn","api:app","--host=0.0.0.0","--reload"]

#FROM python:3.8.8-slim
#RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
#RUN apt-get -y install curl
#RUN apt-get install libgomp1
## copy the local requirements.txt file to the
## /app/requirements.txt in the container
## (the /app dir will be created)
#COPY ./requirements.txt /app/requirements.txt
#RUN pip install --upgrade pip setuptools wheel
## install the packages from the requirements.txt file in the container
#RUN pip install -r /app/requirements.txt
## expose the port that uvicorn will run the app
##EXPOSE 8000:8000
## copy the local app/ folder to the /app fodler in the container
#COPY ./ /app
## set the working directory in the container to be the /app
#WORKDIR /app
#CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]