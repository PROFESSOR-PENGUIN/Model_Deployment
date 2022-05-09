# Deploying a simple Model Locally using Docker and FASTApi
---

### Running without Docker 
---
1. Clone the Repo
   
2. Create a virtual env using command line
    python -m venv venv
   
3. Activate the virtual env by typing into command line
    venv\Scripts\activate
   
4. Install the required libraries using
    pip install -r requirements.txt
   
5. Run api.py file using
    python api.py
   
6. goto http://localhost:8001/docs  and start predicting
   
#### Running with Docker
---
comment out line 51 & 52 in api.py since we are already using CMD directive in Dockerfile
make sure you have docker desktop installed
create an image using the command
1. *** docker build -t docker_model_api . ***
2. Check the Docker desktop when the image is created and run  it

