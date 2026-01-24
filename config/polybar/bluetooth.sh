
#!/bin/bash

# Check if bluetooth is powered on
status=$(bluetoothctl show | grep "Powered: yes" | wc -l)

if [ "$status" -eq 0 ]; then
    echo "%{F#66}󰂲%{F-}" # Greyed out icon if off
else
    # Check if any device is connected
    connected=$(bluetoothctl info | grep "Connected: yes" | wc -l)
    if [ "$connected" -gt 0 ]; then
        echo "%{F#2196F3}󰂱%{F-}" # Blue icon if connected
    else
        echo "󰂯" # Standard icon if on but not connected
    fi
fi
