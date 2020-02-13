.PHONY: build
build:
	docker-compose build roll_the_dice

.PHONY: shell
shell:
	docker-compose run --rm roll_the_dice /bin/bash

.PHONY: test
test:
	docker-compose run --rm roll_the_dice poetry run pytest

.PHONY: lint
lint:
	docker-compose run --rm roll_the_dice bash -c "poetry run black roll_the_dice/ && poetry run flake8 roll_the_dice/ && poetry run mypy roll_the_dice/"

.PHONY: wheel
wheel:
	docker-compose run --rm roll_the_dice poetry build -f wheel
