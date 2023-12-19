
.PHONY: up
up:
	@docker-compose up

.PHONY: down
down:
    @docker-compose down

.PHONY: test
test:
	@docker-compose --compatibility run --rm app pytest tests
