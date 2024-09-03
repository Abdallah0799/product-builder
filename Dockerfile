FROM python:3.9

# Install manually all the missing libraries
RUN apt-get update

# Install pipenv and compilation dependencies
RUN pip install pipenv

#  Create virtual environment directory in WORKDIR (/app) 
ENV PIPENV_VENV_IN_PROJECT 1

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pipenv sync

CMD pipenv run gunicorn -w 4 -b $PORT run:app