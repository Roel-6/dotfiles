#!/bin/bash

# A script to select and connect  to a WI-FI network using rofi and nmcli

# Check if rofi is installed
if ! command -v rofi &> /dev/null
then
  echo "Rofi is not installed."
  exit 1
fi

# Get wifi icons
get_wifi_icons(){
  SIGNAL=$1
  if [ "$SIGNAL" -ge 80 ]; then
    echo "󰤨 "
  elif [ "$SIGNAL" -ge 60 ]; then
    echo "󰤥 "
  elif [ "$SIGNAL" -ge 40 ]; then
    echo "󰤢 "
  elif [ "$SIGNAL" -ge 20 ]; then
    echo "󰤟 "
  else 
    echo "󰤠 "
  fi
}

# Get disconnect option
WIFI_DEVICE=$(nmcli -t -f DEVICE dev | grep -E '^wl')

# Get the name of the currently connected network (SSID)
CONNECTED_SSID=$(nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d ':' -f 2)

# Fetch the list off WI-FI networks with signal strength
WIFIS=$(nmcli -t -f SSID,SIGNAL dev wifi list | while read -r line; do
  if [ -z "$line" ] || [[ $line == "SSID:SIGNAL" ]]; then
    continue
  fi
  SSID=$(echo "$line" | cut -d ':' -f 1)
  SIGNAL=$(echo "$line" | cut -d ':' -f 2)
  if [ -z "SSID" || [ "$SSID" == "$CONNECTED_SSID" ]; then
    continue
  fi
  ICON=$(get_wifi_icons "$SIGNAL")
  echo "$ICON $SSID"
done | sort -u)

DISCONNECT_OPTION=""
if [ -n "$CONNECTED_SSID" ]; then
  DISCONNECT_OPTION="󰤭 Disconnect WI-FI ($CONNECTED_SSID)"
fi

# Combine disconnect option with the list of networks
if [ -n "$DISCONNECT_OPTION" ]; then
  FULL_LIST=$(echo -e "$DISCONNECT_OPTION\n$WIFIS")
else
  FULL_LIST="$WIFIS"
fi

# Use rofi to let the user select a network
if [ -z "$FULL_LIST" ]; then
  rofi -e "No WI-FI networks available."
  exit 0
fi

SELECTED_LINE=$(echo -e "$FULL_LIST" | rofi -dmenu -i -p "WI-FI Networks")

# Exit if selection is empry
if [ -z "$SELECTED_LINE" ]; then
  exit 0
fi

# Handle selection: Disconnect or connect

# Check if the user selected the disconnect option
if echo "$SELECTED_LINE" | grep -q "Disconnect WI-FI"; then
  nmcli device disconnect "$WIFI_DEVICE"
    notify-send "WI-FI" "Disconnected from $CONNECTED_SSID"
  else
    SELECTED_WIFI=$(echo "$SELECTED_LINE" | awk '{print $NF}')
    nmcli device wifi connect "$SELECTED_WIFI"
fi

