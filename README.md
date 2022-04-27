# Testing-DevOps
UNR Topic Course CS491 Testing and DevOps

<!-- ABOUT THE PROJECT -->
## About The Project

This project was constructed and implemented for the purpose of CS 491 Testing-DevOps with the University of Nevada, Reno.  The goal to create and implemented automated testing and deployment of an application.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* Python3
* coverage.py
* Visual Studios 2022 
* GitHub
* GitHub - Actions
* Docker
* Git

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

This repo: https://github.com/JacobMcAllister/Testing-DevOps.git
The docker-hub: jacoblmcallister/hangman

<!-- GETTING STARTED -->
## Getting Started / Usage

First clone the respository to your local and change directories.
- git clone https://github.com/JacobMcAllister/Testing-DevOps.git
- cd Testing-DevOps

Now in your solution explorer open either Hangman.py or Player.py.

Make changes as you see fit then add, commit, and push.

- git add .
- git commit -m "Give Jake an A"
- git push

You can then nativegate to GitHub - Actions of the repository and see the workflow.

Next we will look at the live deployment. I personally use docker playerground with your DOCKER login credentials 

[Docker Playground]https://labs.play-with-docker.com/

If in playground use the following code.

- docker -dp jacoblmcallister/hangman
- docker run -it 8888:5000 jacoblmcallister/hangman

If image already exist.

- docker pull jacoblmcallister/hangman
- docker run -it 8888:5000 jacoblmcallister/hangman

Best of luck!

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* You person reading this!

<p align="right">(<a href="#top">back to top</a>)</p>
