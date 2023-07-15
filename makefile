start:
	@docker-compose up bast-space-service

clean:
	@rm -rf .coverage & rm -rf .pytest_cache & rm -rf .mypy_cache & rm -rf **/__pycache__/** || echo "All clean"

rc-test:
	@python -m pytest -vv --cov-report=term-missing --cov=src --cov-config=setup.cfg --cov-fail-under=90 tests

install:
	@pip install -r requirements.txt

lint:
	flake8 --count --statistics src tests
	mypy --install-types --non-interactive src

test:
	@docker-compose run --rm bast-space-tests flake8 --count --statistics src tests
	@docker-compose run --rm bast-space-tests mypy --install-types --non-interactive src
	@docker-compose run --rm bast-space-tests

start-consumer:
	@docker-compose up subscription-event-consumer-worker

stop:
	@docker-compose down

setup-offers:
	@docker-compose run --rm bast-space-service-partitions

setup-db:
	@docker-compose run --rm bast-space-service-alembic
	@docker-compose run --rm bast-space-service-partitions

data-patches:
	@docker-compose run --rm subscription-data-patches