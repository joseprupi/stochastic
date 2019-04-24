#/bin/bash

fswatch -0 ./ | xargs -0 -n 1 bash ./autocomitmac.sh