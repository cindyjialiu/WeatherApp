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
Unzip the file or clone the repo
If you don't have Django installed, please follow the guide [here](https://docs.djangoproject.com/en/2.1/topics/install/).
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
## How to run the test (backend only)
```bash
./manage.py test 
```

## My Approach

### Learning basics of the new technology
* Due to no experience on Python and Django, before I started the actually project I decided to follow tutorial 
to setup a project to learn the basics.

### Fetch the weather data from API and present it with table

* Work out how to fetch weather data from API [openweathermap](https://openweathermap.org/api), the city 
parameter is hard coded to London currently, it will only show the weather data for London. This part
 was going pretty well, but it took more time to get the data in correct format and put it in the template.
* Make sure all the backend logic been tested properly.
* Spent time on setting up frontend work in React, as lack of experience in React, I spent a lot more time
researching and learning in order to get to the point I can build the project step by step.
* Used react table as the template to link it with the weather data.

### Fetch the weather forecast data from API and present it with bar chart
* This part of the data requires a different API call, but the fetching historical weather data API is not 
available to free account, normally I would search for a different API or seek for a paid account
to achieve it. But for the purpose of this exercise, I decided to use the weather forecast API instead. 
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
* Make the app interactive, so the user can input the city or period of time to search the weather information.
* Building UI

## What went well
* Manage to get the data from the weather API calls and show it on the web page.
* Use table to present the current weather data.
* Use bar chart to show the temperatures across the day.

## What was difficult
* Setting up the project and install the required dependencies.
* All the documentation I've read required node module and also the JSX is used in most examples. When I tried
 to use the table and bar chart libraries, I was struggling to get the imported file working. But in order to balance
 the time spent on learning and doing the project, I decided to just get this working rather than spend too much time on it.
## Summary
In general, I am happy with the result I've got so far and enjoyed the learning experience when I followed tutorial and could
use the new knowledge straightaway. But lots of new things required deeper understanding to achieve a better result, which led to 
frustration and stress. I would prefer to have more support and working in the team.
The biggest difficulty I had was how to balance learning new technology and doing the project, as learning multiple
new things in parallel is not easy. On my coding bootcamp which I finished in May, I only needed to focus on one new 
technology every week with other people, which is a better way for learning. 
