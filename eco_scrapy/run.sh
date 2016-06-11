#!/bin/bash
. ~/bin/pyvenv_scrapy/bin/activate
scrapy runspider ./ecocrackenback.py > output.txt
