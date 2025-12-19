docker run --rm -i \
  -v $(pwd):/src \
  grafana/k6:0.54.0 run /src/script.js