#!/bin/bash

echo "Exporting development dependencies -> requirements.txt..."
pipenv lock --requirements --dev > requirements.txt

