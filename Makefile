build:
	docker compose build
up:
	docker compose up
down:
	docker compose down -v
db:
	docker compose exec db psql --username=$(USERNAME) --dbname=$(DBNAME)
