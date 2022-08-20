FROM python:3.10-slim-bullseye

COPY poetry.lock pyproject.toml $HOME/
COPY swarm_communauto $HOME/swarm_communauto/

RUN pip3 install poetry && \
	poetry install && \
	poetry build && \
	pip3 install dist/*.tar.gz

ENTRYPOINT [ "python3", "-m", "swarm_communauto" ]
