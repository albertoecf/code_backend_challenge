
.PHONY: up
up:
	@docker-compose up

.PHONY: test
test:
	@docker-compose --compatibility run --rm app pytest tests
