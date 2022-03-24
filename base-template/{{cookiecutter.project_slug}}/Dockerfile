# Contact me:
#   e-mail:   enrique@enriquecatala.com 
#   Linkedin: https://www.linkedin.com/in/enriquecatala/
#   Web:      https://enriquecatala.com
#   Twitter:  https://twitter.com/enriquecatala
#   Support:  https://github.com/sponsors/enriquecatala
#   Youtube:  https://www.youtube.com/enriquecatala
#

#############################################################################
# 1/2 COMPILE-IMAGE
#
FROM ubuntu:20.04 as compile-image

### Install python
#
RUN apt-get update && apt-get install -y python3-pip python3-venv

# Compilation environment build 
RUN python3 -m venv /opt/venv
# Update $PATH to get priority from /opt/venv/bin path
ENV PATH="/opt/venv/bin:$PATH"

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
#
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt 

#################################
# DOWNLOAD YOUR MODEL
#
RUN apt-get update && apt-get -y install unzip
RUN mkdir -p /app/ai_model

#################################

###########################################################################
# 2/2 RELEASE IMAGE
#
# After the build, new container
FROM ubuntu:20.04 as release

LABEL  "MAINTAINER" "{{ cookiecutter.full_name }}<{{ cookiecutter.email }}>"
LABEL "Project" "{{ cookiecutter.project_name }}"
LABEL project="{{ cookiecutter.project_name }}" role="{{ cookiecutter.project_role }}" sku="cpu"

EXPOSE 80

### Install python
#
RUN apt-get update && apt-get install -y python3-pip python3-venv

# Copy dependencies from compile-image
COPY --from=compile-image /opt/venv /opt/venv
COPY --from=compile-image /app /app

# Update $PATH to get priority from /opt/venv/bin path
ENV PATH="/opt/venv/bin:$PATH"

COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

#################################
# Setup your code
WORKDIR /app
COPY . /app

ENV PYTHONPATH=/app

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd appuser -m -d /home/appuser/ &&  chown -R appuser /app
USER appuser
#################################


# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]

