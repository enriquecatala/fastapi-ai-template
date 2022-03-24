"""
 Contact me:
   e-mail:   enrique@enriquecatala.com 
   Linkedin: https://www.linkedin.com/in/enriquecatala/
   Web:      https://enriquecatala.com
   Twitter:  https://twitter.com/enriquecatala
   Support:  https://github.com/sponsors/enriquecatala
   Youtube:  https://www.youtube.com/enriquecatala
   
"""

from starlette.config import Config
from starlette.datastructures import Secret
import os

APP_VERSION = "{{ cookiecutter.version }}"
APP_NAME = "{{ cookiecutter.container_name }}"
API_PREFIX = "/api"

# if __debug__:
#   config = Config(".env")

#   API_KEY: Secret = config("API_KEY", cast=Secret)
#   IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

#   DATA_PATH: str = config("DATA_PATH")

#   APPLICATION_INSIGHTS_KEY: str = config("APPLICATION_INSIGHTS_KEY")
#   print ("IFF +++++++++++++++++++++++++++++++++++++++++++++")
# else:
API_KEY: Secret = os.environ.get("API_KEY")
IS_DEBUG: bool = os.environ.get("IS_DEBUG", False)
DATA_PATH: str = os.environ.get("DATA_PATH")
APPLICATION_INSIGHTS_KEY: str = os.environ.get("APPLICATION_INSIGHTS_KEY")