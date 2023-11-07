#!/bin/bash
MESSAGE="=====ALERTA $2===== $1$2 $7$8 $3$4 ${11}${12} $9${10} ${13}${14} $5$6 ${15}${16} =====FIN ALERTA====="
source /home/scfctrm/.bash_profile
# Curl command
curl -X POST "https://http-intake.logs.datadoghq.eu/api/v2/logs" -H "Accept: application/json" -H "Content-Type: application/json" -H "DD-API-KEY:${DD_API_KEY}" -d "{\"ddsource\":\"helix_controlm\",\"message\":\"$MESSAGE\"}"
# End of script
exit 0