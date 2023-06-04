FROM python:3.7

WORKDIR /opt/roll-the-dice

# install poetry to container
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

# build project env
COPY ./pyproject.toml /opt/roll-the-dice/pyproject.toml
RUN poetry install
