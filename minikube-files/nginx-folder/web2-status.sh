#!/bin/bash
kubectl -n dev get pod web2  -o jsonpath={.status.phase}

#make it executable

chmod +x web2-status.sh