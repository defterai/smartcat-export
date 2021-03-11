FROM debian:stable-slim

LABEL "maintainer"="Defter"
LABEL "repository"="https://github.com/defterai/smartcat-export"
LABEL "version"="0.1.0"

COPY smartcat.py /smartcat.py
COPY export-smartcat.py /export-smartcat.py
COPY entrypoint.sh /entrypoint.sh

RUN apt-get update; \
    apt-get install -y python3; \
    apt-get clean -y; \
    rm -rf /var/lib/apt/lists/*; \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]