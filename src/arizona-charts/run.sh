#!/bin/bash

sudo docker run --name arizona-charts-covid19 \
    -v "$PWD"/sandbox:/work \
    -it \
    --net=host \
    arizona-charts-covid19
