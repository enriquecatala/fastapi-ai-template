#!/bin/bash

# Contact me:
#   e-mail:   enrique@enriquecatala.com 
#   Linkedin: https://www.linkedin.com/in/enriquecatala/
#   Web:      https://enriquecatala.com
#   Twitter:  https://twitter.com/enriquecatala
#   Support:  https://github.com/sponsors/enriquecatala
#   Youtube:  https://www.youtube.com/enriquecatala

# NOTE:
# -----
# Debug will override this by creating only 1 Worker
#

MODULE=app.main
APP=app      
NAME={{ cookiecutter.project_slug }}



#WORKER_THREADS: between 2-4 per core: https://docs.gunicorn.org/en/latest/settings.html?highlight=workers#workers

uvicorn ${MODULE}:${APP}        \
         --port 5000       \
         --host 0.0.0.0 \
         --workers $WORKER_THREADS
         

