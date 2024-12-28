#!/usr/bin/sh

poetry run long_task_1 &
PID_1=$!

poetry run long_task_2 &
PID_2=$!

wait $PID_1
wait $PID_2
