#!/bin/bash

if [[ $(mysql -u root -p freewave < ~/query.sql | tail -n +2) ]]; then
	echo "$(mysql -u root -p freewave < ~/query.sql | tail -n +2)"
else
	echo "No harmful dates found!"
fi
