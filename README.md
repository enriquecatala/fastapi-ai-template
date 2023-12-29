<div class="social_links">
    <a href="https://www.clouddataninjas.com"><img src="https://img.shields.io/website?down_color=red&down_message=down&label=clouddataninjas.com&up_color=46C018&url=https%3A%2F%2Fwww.clouddataninjas.com&style=for-the-badge" alt="Cloud Data Ninjas"></a>
    <a href="https://github.com/enriquecatala" target="_blank"><img  src="https://img.shields.io/github/followers/enriquecatala?label=GitHub&style=for-the-badge" alt="GitHub followers of Enrique Catalá" ></a>
    <a href="https://github.com/sponsors/enriquecatala" target="_blank"><img src="https://img.shields.io/badge/GitHub_Sponsors--_.svg?style=for-the-badge&logo=github&logoColor=EA4AAA" alt="Sponsor Enrique Catalá on GitHub" ></a>    
    <a href="https://www.linkedin.com/in/enriquecatala" target="_blank"><img src="https://img.shields.io/badge/LinkedIn--_.svg?style=for-the-badge&logo=linkedin" alt="LinkedIn Enrique Catalá" ></a>        
    <a href="https://twitter.com/enriquecatala" target="_blank"><img src="https://img.shields.io/twitter/follow/enriquecatala?color=blue&label=twitter&style=for-the-badge" alt="Twitter @enriquecatala" ></a>    
    <a href="https://enriquecatala.com"><img src="https://img.shields.io/website?down_color=red&down_message=down&label=enriquecatala.com&up_color=46C018&url=https%3A%2F%2Fenriquecatala.com&style=for-the-badge" alt="Data Engineering with Enrique Catalá"></a>
    <a href="https://youtube.com/enriquecatala"><img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/youtube.png" alt="Canal de Enrique Catalá" height=20></a>
</div> 

<div style="display: flex; align-items: left; justify-content: left;">
  <a href="https://www.credly.com/badges/cde0dbd2-8d03-4ca7-8284-d471d65d0e5f">
      <img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/MVP_Logo_horizontal.png" 
           alt="Microsoft DataPlatform and AI MVP Enrique Catalá"
           style="min-height: 50px; max-height: 70px; min-width: 100px">
  </a>
  <a href="https://www.clouddataninjas.com">
          <img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala.github.io/master/img/CLOUDDATANINJAS.png" 
          alt="Cloud Data Ninjas" 
          style="min-height: 50px; max-height: 70px; min-width: 250px "/>
  </a>
</div>

- [fastapi-ai-template](#fastapi-ai-template)
  - [What is included on this template?](#what-is-included-on-this-template)
  - [Setup](#setup)
    - [Install cookiecutter](#install-cookiecutter)
    - [FastAPI base template](#fastapi-base-template)
    - [FastAPI + spacy template](#fastapi--spacy-template)
    - [FastAPI + huggingface template](#fastapi--huggingface-template)
    - [Configuration](#configuration)
    - [Project template parameters](#project-template-parameters)

> Author: [Enrique Catalá Bañuls](https://www.linkedin.com/in/enriquecatala)
# fastapi-ai-template
FastAPI ai templates to deploy AI models. ❤️ [Sponsor this project](https://github.com/sponsors/enriquecatala)

You **don´t need to fork this project**. This project is a template for cookiecutter that can be [used directly from your command line without forking it](#setup). The output of this project is a fully configured FastAPI application ready for you to start coding and deploy.


## What is included on this template?

🖼️ The base to start an openapi project for AI: [spacy](#create-your-own-fastapi-for-spacy)/huggingface, FastAPI.

🐋 A Dockerfile+docker-compose to build the container image for your project.
If you want to contribute to this template please open an issue or fork and send a PULL REQUEST.

⏯ Visual studio code _launch.json_ and _tasks.json_ to [debug the project in VS Code with container support](https://docs.microsoft.com/en-us/visualstudio/containers/edit-and-refresh?view=vs-2022)




## Setup

Since this is a template for cookiecutter, you need first to install cookiecutter.
### Install cookiecutter

This template requires [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) to be [installed](https://cookiecutter.readthedocs.io/en/latest/installation.html).

### FastAPI base template

Once [installed](https://cookiecutter.readthedocs.io/en/latest/installation.html), you can run the following command to create a new project:

```bash
# go to the directory where you want to create the project
cd ~
mkdir your-project
cd your-project
# create your project using this template
cookiecutter https://github.com/enriquecatala/fastapi-ai-template.git \
             -v \
             --directory="base-template"
```

This will create a base ApiREST project ready for you to test and deploy. It will include a _test method_ that you can use to test your code.

```bash
docker compose build
docker compose up
```
Now navigate to http://127.0.0.1:5000/docs to see the documentation.



### FastAPI + spacy template
Once [installed](https://cookiecutter.readthedocs.io/en/latest/installation.html), you can run the following command to create a new project:

```bash
# go to the directory where you want to create the project
cd ~
mkdir your-project
cd your-project
# create your project using this template
cookiecutter https://github.com/enriquecatala/fastapi-ai-template.git \
             -v \
             --directory="spacy-template"
```

### FastAPI + huggingface template

TODO
### Configuration

After asking you for parameter configuration values, it will create the following files:
```bash
your-project/
├── fastapi-ai-template/  <--------- Project template 
    └── .vs-code/         <--------- visual studio debug config 
        ├── launch.json        
        └── tasks.json
    └── app/              <--------- Project folder 
        ├── api/          <--------- api routing
        ├── core/         <--------- event handling and security
        ├── models/       <--------- Model classes definition
        ├── services/     <--------- API main methods (this is where you have the main logic)
        └── main.py
    ├── Dockerfile 
    ├── docker-compose.yml 
    ├── gunicorn_conf.py  <--------- web server config
    ├── requirements.txt  <--------- default libraries
    └── ...    
```

### Project template parameters

Executing the cookiecutter command **will ask you in the command prompt** for all the parameters defined in the [cookiecutter.json](spacy-template/cookiecutter.json) file. Default values are the following:

```json
{
    "full_name": "Enrique Catalá Bañuls",
    "email": "enrique@enriquecatala.com",
    "project_name": "FastAPI AI template",
    "project_slug": "{{ cookiecutter.project_name|lower|replace(' ', '-') }}",
    "project_role": "fastapi API",
    "container_name": "fastapi-ecb-api",
    "port": "5000",
    "repo_name": "fastapi-ai-template",
    "project_short_description": "FastAPI template generator for AI projects. It generates a template for a FastAPI project with a simple and easy to use interface.",        
    "version": "0.1.0",
    "application_insights_key": "USE A VALID APP INSIGHTS KEY",
    "api_key": "WRITE YOUR OWN API KEY :)",
    "_copy_without_render": [      
      "model-best"
  ]
  }
```

>NOTE: For more tips, please [check the docs](https://cookiecutter.readthedocs.io/en/latest/usage.html).
