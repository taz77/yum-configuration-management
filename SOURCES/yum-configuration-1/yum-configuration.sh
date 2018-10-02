#!/bin/bash
source /etc/yum-configuration/yum-configuration-output.conf

if [[ -z "$device" ]]; then
  echo "Device"
  read devicename
else
  devicename="$device"
fi

ip4=$(/sbin/ip -o -4 addr list $device | awk '{print $4}' | cut -d/ -f1)
DATE=`date +%Y%m%d`

if [[ -z "$destination" ]]; then
  echo "Destination"
  read destinationname
else
  destinationname="$destination"
fi



yum list installed > $destinationname/$ip4.$DATE.package.list.txt
