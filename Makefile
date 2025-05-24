.PHONY: run clean up down rebuild deepclean start stop build

# Run project to build files, then stop and remove container
run:
	@echo ""
	@echo "=================================================="
	@echo "Building and running project..."
	@echo "=================================================="
	@echo ""
	@docker-compose run --rm app
	@echo ""
	@echo "=================================================="
	@echo "Project Complete. See ./output folder for results"
	@echo "=================================================="
	

# Start services
up start build:
	docker-compose up --build -d
	

# Stop services
down stop:
	docker-compose down

# Rebuild everything from scratch
rebuild:
	docker-compose down
	docker-compose up --build -d
	

# Remove generated files (images, reports, CSVs)
clean:
	rm -f output/*.csv output/*.png output/*.md

# Complete clean slate, but potentially destructive
deepclean:
	rm -f output/*.csv output/*.png output/*.md
	docker-compose down --volumes