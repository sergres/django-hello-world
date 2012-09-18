#!/bin/bash
 
./manage.py list_models 1>/dev/null 2>&1  >    `date +%Y-%m-%d`.dat
