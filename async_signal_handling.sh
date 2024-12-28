#!/bin/bash

PID_1=-1

# a callback function to handle the signals
cleanup() {
    echo "Caught a signal. Cleaning up..."
    kill -TERM "$PID_1"
    exit 0
}

# set the callback
trap cleanup HUP INT QUIT ABRT

# detach a task
(
while true; do
    echo "Running..."
    sleep 1
done
) &

PID_1=$!

wait "$PID_1"
