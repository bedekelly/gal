#!/bin/bash

pyclean () {
	find . -name "*~" -exec rm {} \; && find . -name "*.pyc" -exec rm {} \; && find . -name "__pycache__" -exec rm -r {} \; 2> /dev/null
	true
}

# Clean python and node/yarn/webpack gunk.
pyclean
rm -rf venv frontend/node_modules frontend/dist frontend/yarn-error.log
