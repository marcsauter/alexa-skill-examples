#!/bin/bash

cd ./presentations
present -notes -base ../www -http=$(hostname):8080
