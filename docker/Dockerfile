FROM --platform=linux/amd64 python:3.11.1-buster

# install time zone
ENV TZ="Europe/Moscow"
RUN apt-get install -y tzdata
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# Install pyodbc dependencies
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev tdsodbc g++ unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt install unixodbc-dev -y
RUN apt-get clean -y
ADD odbcinst.ini /etc/odbcinst.ini

# Install the Microsoft ODBC driver for SQL Server (Linux)
# https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15
RUN apt-get update
RUN apt-get install apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Add path
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# install library
RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# copy all files to /app directory and move into directory.
COPY . /app
WORKDIR /app

CMD ["python", "main.py"]