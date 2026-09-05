# Selenium Python + Pytest + Jenkins Practice Project

A small Page Object Model project designed for PyCharm -> GitHub -> Jenkins practice.

## Project flow

PyCharm -> Git -> GitHub -> Jenkins -> pip install -> pytest -> Selenium -> HTML report

## Local setup

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
pytest
```

The tests use the public SauceDemo practice application.

## Standard practice credentials

Username: `standard_user`
Password: `secret_sauce`

## Jenkins

The included `Jenkinsfile` is intended for a Windows Jenkins agent.
It installs dependencies, runs pytest, and publishes the HTML report.

For the first Jenkins exercise, you can also copy the Jenkinsfile contents into
a Pipeline job using "Pipeline script from SCM" after pushing this project to GitHub.

SCM Polling test - Jenkins automatically detects GitHub changes.