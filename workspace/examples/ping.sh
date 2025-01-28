#!/bin/sh

IP=${1:-8.8.8.8}
ping -c 200 "$IP"