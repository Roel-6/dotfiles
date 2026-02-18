#!/bin/bash

# Load colors from pywal
. "${HOME}/.cache/wal/colors.sh"

# grabs the wallpaper and resize it
WAL=`cat ~/.cache/wal/wal`
RESIZE="/tmp/screenlock.png"

# Get the current hour and username
HOUR=$(date +%H)
HOUR_INT=$((10#$HOUR))
USER=$(whoami)

if [ "$HOUR_INT" -ge 0 ] && [ "$HOUR_INT" -lt 5 ]; then
    MSG="Working late, aren't we $USER?"
elif [ "$HOUR_INT" -ge 5 ] && [ "$HOUR_INT" -lt 12 ]; then
    MSG="Good morning, $USER!"
elif [ "$HOUR_INT" -ge 12 ] && [ "$HOUR_INT" -lt 18 ]; then
    MSG="Good afternoon, $USER!"
else
    MSG="Good evening, $USER!"
fi

# Lock with transparent background and pywal ring colors
i3lock                              \
  --color="${background}40"         \
  -i "$RESIZE"                      \
  --inside-color="${color0}BF"      \
  --insidever-color="${color3}BF"   \
  --ring-color="$color7"            \
  --ringver-color="${color6}"       \
  --keyhl-color="$color1"           \
  --bshl-color="$color6"            \
  --verif-color=#00000000           \
  --wrong-color=#00000000           \
  --radius=40                       \
  --indicator                       \
  --ind-pos="150:680"               \
  --force-clock                     \
  --time-font=Iosevka               \
  --time-color="$foreground"        \
  --time-align=1                    \
  --time-size=60                    \
  --date-font=Iosevka               \
  --date-color="$color5"            \
  --date-align=1                    \
  --date-size=30                    \
  --time-pos="220:688"              \
  --greeter-text="$MSG"             \
  --greeter-font=Iosevka Nerd Font  \
  --greeter-color="$color6"         \
  --greeter-align=1                 \
  --greeter-size=60                 \
  --greeter-pos="100:150"


