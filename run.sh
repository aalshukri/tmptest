#!/bin/sh
docker run -it --mount src=`pwd`,target=/project,type=bind python-app