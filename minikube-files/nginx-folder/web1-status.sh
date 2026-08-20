#!/bin/bash
kubectl -n application get pod web1  -o jsonpath={.status.phase}

#make it executable

chmod +x web1-status.sh