#!/bin/bash


echo "Waiting for MySQL..."
sleep 20

# now run project
exec python analyze_survey.py
    
# replace with "generate_report.py" later
