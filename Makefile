.PHONY: run clean down rebuild deepclean start stop

# Start services
run start:
	docker-compose up --build

# Stop services
down stop:
	docker-compose down

# Rebuild everything from scratch
rebuild:
	docker-compose down
	docker-compose up --build

# Remove generated files (images, reports, CSVs)
clean:
	rm -f output/*.csv output/*.png output/*.md

# Complete clean slate, but potentially destructive
deepclean:
	rm -f output/*.csv output/*.png output/*.md
	docker-compose down --volumes