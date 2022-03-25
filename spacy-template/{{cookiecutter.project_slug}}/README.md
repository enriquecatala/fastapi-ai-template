<div>
    <a href="https://github.com/sponsors/enriquecatala"><img src="https://img.shields.io/badge/GitHub_Sponsors--_.svg?style=flat-square&logo=github&logoColor=EA4AAA" alt="GitHub Sponsors"></a>
    <a href="https://enriquecatala.com"><img src="https://img.shields.io/website?down_color=red&down_message=down&label=enriquecatala.com&up_color=46C018&url=https%3A%2F%2Fenriquecatala.com&style=flat-square" alt="Data Engineering with Enrique Catalá"></a>
    <a href="https://www.linkedin.com/in/enriquecatala"><img src="https://img.shields.io/badge/LinkedIn--_.svg?style=flat-square&logo=linkedin" alt="LinkedIn Enrique Catalá Bañuls"></a>
    <a href="https://twitter.com/enriquecatala"><img src="https://img.shields.io/twitter/follow/enriquecatala?color=blue&label=twitter&style=flat-square" alt="Twitter @enriquecatala"></a>
    <a href="https://youtube.com/enriquecatala"><img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/youtube.png" alt="Data Engineering: Canal youtube de Enrique Catalá" height=20></a>
</div>

<a href="https://mvp.microsoft.com/es-es/PublicProfile/5000312?fullName=Enrique%20Catala"><img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/MVP_Logo_horizontal.png" alt="Microsoft DataPlatform MVP Enrique Catalá"></a>

- [{{ cookiecutter.project_slug }}](#-cookiecutterproject_slug-)
  - [Setup](#setup)
    - [Optional performance parameters](#optional-performance-parameters)
  - [Setup your model](#setup-your-model)
  - [Test your API](#test-your-api)

>Author: [Enrique Catalá](https://www.linkedin.com/in/enriquecatala)
# {{ cookiecutter.project_slug }}

This RestAPI app has been created using [FastAPI base template](https://github.com/enriquecatala/fastapi-ai-template). 

>Please consider ❤️ [Sponsoring this project](https://github.com/sponsors/enriquecatala)

This is the template I use to expose my own deep neural networks in production.

This project includes a template for expose an Artificial Inteligence model composed by your own keras model, through a FastAPI API Rest configuration **ready for production**.

The output is a container ready to **deploy in your kubernetes cluster**.

## Setup

1. In the docker-compose.yml, go and configure the API_KEY. <br>
   A sample API key can be generated using Python REPL:
```python
import uuid
print(str(uuid.uuid4()))
```

### Optional performance parameters

You can fine tune your webserver by configuring the [boot.sh](boot.sh)

## Setup your model

Go to the [services/models.py](app/services/models.py) and add your own code

## Test your API

1. Go to http://127.0.0.1:{{ cookiecutter.port }}/docs
2. Click on the "lock" icon 
   
   ![lock icon](assets/images/lock.png)
3. Write your API key
   
   ![api-key](assets/images/api-key.png)
   
4. Have fun!
