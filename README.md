Ruffly following [DjangoX tutorial](https://learndjango.com/tutorials/django-blog-tutorial) | [GitHub](https://github.com/wsvincent/djangox)


## Project setup and initial stuff

### File structure "flow"
```mermaid
flowchart TD
    subgraph django_app
        M[models.py]
        Ad["admin.py\nadmin.site.register(Model)"]
        V[views.py]
        T[templates/*.html]
        Ua[urls.py]
    end

    subgraph django_project
        S["settings.py\nINSTALLED_APPS = []"]
        Up[urls.py]
    end
    
    django_app -- add to ---> S
    M -- import models --> Ad
    M -- import models --> V
    V -- import views --> Ua
    Ua -- include url --> Up
    T  -- used in --> V
```
### Init, create, migrate, develop, run flow
```mermaid
flowchart TD
    subgraph init[Initial app setup - create project]
        s0[$ python -m pip install django]
        s1["$ django-admin startproject &lt;project_name&gt; &lt;project_directory&gt;"]
        s2[$ python manage.py migrate]
        su[python manage.py createsuperuser]
        s0 --> s1 --> s2 --> su
    end
    
    subgraph run[Run development server]
       ex[$ python manage.py runserver]
    end
    
    subgraph create_app[Create app]
        s3["$ python manage.py startapp &lt;app_name&gt;"]
    end
    
    subgraph migrate[Migrate database to new models]
        s4[$ python manage.py makemigrations]
        s5[$ python manage.py migrate]
        s4 --> s5
    end
    
    dev[Development]
    
    init --> run
    init --> create_app
    create_app --> dev
    dev --> migrate --> run
    run --> dev
    dev --> run
    
```