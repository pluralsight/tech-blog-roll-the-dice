FROM python:3.7

WORKDIR /opt/roll-the-dice

# install poetry to container
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH /root/.poetry/bin:$PATH

# build project env
COPY ./pyproject.toml /opt/roll-the-dice/pyproject.toml
RUN poetry install
