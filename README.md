# WeatherApp

## User story
As a user, I want to be able to see the minimum, maximum, average, temperature and humidity for a given city and period of time.

## Technology Used
### Backend
* Language: Python
* Framework: Django
### Frontend
* React
* JavaScript
## Setup(for mac)
* Unzip the file or clone the repo
* If you don't have Django installed, please follow the guide [here](https://docs.djangoproject.com/en/2.1/topics/install/).
```bash
git clone: git@github.com:cindyjialiu/WeatherApp.git 
```
```bash
npm install
cd WeatherApp
# To start the server locally
./manage.py runserver 
```
Open http://127.0.0.1:8000/weather/ in your browser and you should see below
## How to run the test
```bash
./manage.py test 
```

## My Approach

### Learning basics of the new technology
* Due to no experience on Python and Django, I decided to setup a dummy project to learn the basics and 
get familiar with them in order to make the first step.

### Fetch the weather data from API and present it with table

* Work out how to fetch weather data from API [openweathermap](https://openweathermap.org/api), the city 
parameter is hard coded to London currently, it will only show the weather data for London. This part
 was going pretty well, but it took more time to get the data in correct format and put it in the template.
* Make sure all the backend logic been tested properly, followed test driven development.
* Spent time on setting up frontend work in React, as lack of experience in React, I spent a lot more time
researching and learning in order to get to the point I can build the project step by step.
* Used react table as the template to link it with the weather data.

### Fetch the weather forecast data from API and present it with barchart
*

## What I have learnt

### Python and Django
* Before - Never used
* With the practise of this project, I only learnt enough to get the basical work done, I would like
 to spend more time to follow the tutorial and get better understanding of these.
### React
* Before - Only worked on a couple of tickets to implement features with existing code base, but never
setup react project from scratch.
* I also would like to practise more on building small projects and gain more knowledge systematically.

## Future work
* Need to write tests for frontend and add more unit tests for the backend logic.
* Making barchart to be responsive.
* Not sure if the current structure of index.html is the proper way to do it, so I would prefer to 
separate the JavaScript/Python code from html.
* Make the app interactive, so the user can input the city or period of time to search the weather inforamtion.
* Building UI

## What went well
* Manage to get the data from the weather API calls and show it on the webpage.
* Use table and barchart to show the present the weather data.

## What was difficult
* Setting up the project
## How to run
