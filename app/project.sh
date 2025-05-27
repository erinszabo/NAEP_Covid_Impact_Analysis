#!/bin/bash


echo "Waiting for MySQL..."
sleep 10

# now run project
exec python generate_report.py
    
