# Docker-python-flask
this project demostrate the ability to build docker image of pythin flask code  using docker file 
#command to freeze all the libaries into requirement.tst
$ $ pip freeze > requirement.tst

#this is the command to build docker image 
$docker build -t daveimage .
#this is the command to list the number of docker images i have locally on my machine 
$ docker images
