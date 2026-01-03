########################################################
# Build Images
########################################################

build-base:
	docker compose build base

images: build-base
	docker compose build ui --no-cache
	docker compose build server --no-cache

########################################################
# Run Images
########################################################

api:
	docker compose up ui server