#!/bin/bash
python main.py --mode="prediction"
python mainMetro.py --mode="prediction"
echo "metro pred"
python mainPark.py --mode="prediction"
python mainStreet.py --mode="prediction"
echo "metro pred"

