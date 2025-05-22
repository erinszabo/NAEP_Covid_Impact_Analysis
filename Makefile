# Makefile for managing the survey-data-project

.PHONY: run clean down rebuild export-csv test

# Start services
run:
	docker-compose up --build

# Stop services
down:
	docker-compose down

# Rebuild everything from scratch
rebuild:
	docker-compose down
	docker-compose up --build

# Remove generated files (images, reports, CSVs)
clean:
	rm -f output/*.csv output/*.png output/*.md

