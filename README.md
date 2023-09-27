# planets-fact-site

## Introduction
This is a multi-page website containing information about the planets of our solar system. This is a practice build to try out Django framework.

The focus will be a simple site in order to work with the basic features including

* models
* Views
* Templates
* Routing

The design for this project was taken from www.frontendmentor.io the planet fact site challenge. (see resources below for links)

## Requirements

* Should follow progressive enhancement and work without JavaScript enabled
* Will use SQLite for its database
* Should work responsively aligning with designs for mobile, tablet and desktop
* Include progressively enhanced tabs component to allow users to switch between content for each planet (overview, internal structure, surface geology)

## Setup project

After checking out the repo jump into the project folder and run the following command

```python
make setup-venv
```

This will setup the project's virtual envrionment, next run the following

```python
source env/bin/activate
```

This will activate the current project in your terminal session making sure you dependencies are installed to the correct location on your system. Next run the following.

```python
make install-packages
```

This will install all your dependencies and finally to test the project is setup run the following.

```python
make run-server
```

This will launch your local development server.

## Resources

* design files: https://www.frontendmentor.io/challenges/planets-fact-site-gazqN8w_f
