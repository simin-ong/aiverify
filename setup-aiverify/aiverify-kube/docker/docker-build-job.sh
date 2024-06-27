#!/bin/bash

docker buildx build --platform linux/amd64 --progress=plain ${@:1} -t aiverify-job:new ./job

