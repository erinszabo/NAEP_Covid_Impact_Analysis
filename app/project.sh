#!/bin/bash


echo "Waiting for MySQL..."
sleep 10

# now run project
exec python create_visuals.py
    
# replace with "generate_report.py" later
