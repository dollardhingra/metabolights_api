# metabolights_api

## Instructions to Setup
There are two ways to setup this app. The first way is simple using docker. 
The second way may be complex without docker


### Method 1: Using Docker (Recommended)
- Install Docker and docker compose on your system
- clone this repo
- go to the root of the app and type:
```
    docker-compose build
    docker-compose up
```
Everything should hopefully work. If things dont work, feel free to shoot an email

### Method 2: Without Docker
- use python 3.7 to create a virtual env 
- clone this repo
- install the requirements using the requirements.txt file
- Make sure you have postgres installed in your system
- if you have problems setting up postgres, use sqlite(you will have to edit the settings)


## Loading fixture data
There is some data which I have provided as initial data. Use the following command to 
import data:
```
docker-compose run app sh -c "python manage.py loaddata fixtures/initial_data.json"
```

## Running the project
There are 2 parts to run the project. The first is running the tests and the second is
running APIs.

### Running tests
To run tests
```
docker-compose run app sh -c "python manage.py test"
```
Kindly note that, the coverage is not 100% currently, I had to skip up tests for file upload
because of time constraint

### APIs
Accessing the APIs is very easy. You can use django rest framework's swagger to do 
API operations. Do the following to access the API:

- Start the container if not already running
```
docker-compose up
```

- List All studies
[localhost:8000/api/study/](localhost:8000/api/study/)

- Study Detail
[localhost:8000/api/study/1](localhost:8000/api/study/1)

- Create study: 
Go to 
[localhost:8000/api/study/](localhost:8000/api/study/) and use the HTML form to create a new study

- List all StudyFiles
[localhost:8000/api/study/studyFile](localhost:8000/api/study/studyFile/)

- If study file doesnt exists
[localhost:8000/api/study/studyFile](localhost:8000/api/study/studyFile/) and use the HTML form to upload a new studyfile
The size limit is 1MB and only text and csv files are allowed

- Filter study files by study id
[localhost:8000/api/study/studyFile?study=1](localhost:8000/api/study/studyFile?study=1)

Apart from these feel free to do similar operations on Authors, Keyword and Publications:
[localhost:8000/api/author/](localhost:8000/api/author/)
[localhost:8000/api/study/keywords](localhost:8000/api/study/keywords/)
[localhost:8000/api/study/publications](localhost:8000/api/study/publications/)


