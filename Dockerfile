FROM python:3.8

# set a directory for the app
WORKDIR C:\Users\Mcall\OneDrive\Documents\GitHub\class-activity4-mcallister-facque

# copy all the files to the container
COPY . .

RUN pip install Flask==2.0.3

EXPOSE 5000

# run the command
CMD ["python", "./Hangman.py"]
