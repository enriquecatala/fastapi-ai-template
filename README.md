<div>
    <a href="https://github.com/sponsors/enriquecatala"><img src="https://img.shields.io/badge/GitHub_Sponsors--_.svg?style=flat-square&logo=github&logoColor=EA4AAA" alt="GitHub Sponsors"></a>
    <a href="https://enriquecatala.com"><img src="https://img.shields.io/website?down_color=red&down_message=down&label=enriquecatala.com&up_color=46C018&url=https%3A%2F%2Fenriquecatala.com&style=flat-square" alt="Data Engineering with Enrique Catalá"></a>
    <a href="https://www.linkedin.com/in/enriquecatala"><img src="https://img.shields.io/badge/LinkedIn--_.svg?style=flat-square&logo=linkedin" alt="LinkedIn Enrique Catalá Bañuls"></a>
    <a href="https://twitter.com/enriquecatala"><img src="https://img.shields.io/twitter/follow/enriquecatala?color=blue&label=twitter&style=flat-square" alt="Twitter @enriquecatala"></a>
    <a href="https://youtube.com/enriquecatala"><img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/youtube.png" alt="Data Engineering: Canal youtube de Enrique Catalá" height=20></a>
</div>

<a href="https://mvp.microsoft.com/es-es/PublicProfile/5000312?fullName=Enrique%20Catala"><img src="https://raw.githubusercontent.com/enriquecatala/enriquecatala/master/img/MVP_Logo_horizontal.png" alt="Microsoft DataPlatform MVP Enrique Catalá"></a>

- [fastapi-ai-template](#fastapi-ai-template)
  - [What is included on this template?](#what-is-included-on-this-template)
  - [Setup](#setup)
    - [Install cookiecutter](#install-cookiecutter)
    - [Create your own fastapi for spacy](#create-your-own-fastapi-for-spacy)

# fastapi-ai-template
FastAPI ai templates to deploy AI models.

You **don´t need to fork this project**. This project is a template for cookiecutter that can be used directly from your command line. The output of this project is a fully configured FastAPI application ready for you to start coding and deploy.


## What is included on this template?
🖼️ The base to start an openapi project for AI: spacy/huggingface, Typer, FastAPI.
🐋 A Dockerfile to build a container image for your project.
If you want to contribute to this template please open an issue or fork and send a PULL REQUEST.

❤️ [Sponsor this project](https://github.com/sponsors/enriquecatala)



## Setup

Since this is a template for cookiecutter, you need first to install cookiecutter.
### Install cookiecutter

This template requires [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) to be [installed](https://cookiecutter.readthedocs.io/en/latest/installation.html).

### Create your own fastapi for spacy
Once [installed](https://cookiecutter.readthedocs.io/en/latest/installation.html), you can run the following command to create a new project:

```bash
cd ~
mkdir your-project
cd your-project
cookiecutter https://github.com/enriquecatala/fastapi-ai-template.git -v --directory="spacy-template"
```

this will create the 
```bash
your-project/
├── fastapi-ai-template/  <--------- Project template 
    └── ...
```

Executing the cookiecutter command will ask you for some information. The default values are stored inside the [cookiecutter.json](spacy-template/cookiecutter.json) file, so you can edit it or type accordingly the values you want from the command promt.

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
    "application_insights_key": "a589f195-43c0-478d-bd95-bd3c9867d597",
    "api_key": "dfaed9ad-e157-49cx-8459-4ecafe134067",
    "_copy_without_render": [      
      "model-best"
  ]
  }
```

>NOTE: For more tips, please [check the docs](https://cookiecutter.readthedocs.io/en/latest/usage.html).
