SERVICE='temperature.service'

if systemctl is-active --quiet $SERVICE; then
  echo "service $SERVICE is active"
else
  echo "service $SERVICE is not active, trying to restart"
  sudo systemctl restart $SERVICE
  if systemctl is-active --quiet $SERVICE; then
    echo"service $SERVICE restarted successfully"
  else
    echo"service $SERVICE could not be restarted"
  fi
fi
