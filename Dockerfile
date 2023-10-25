FROM ruby:3.2.2-slim

# nodejs, yarn install
RUN apt update && apt install -y sudo ca-certificates curl gnupg && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    NODE_MAJOR=20 && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list && \
    apt update && apt install -y nodejs && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt update && apt install -y yarn unzip libpq-dev git make tzdata cron cronutils g++ imagemagick vim gnupg2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ARG UID=1001
ARG GID=1001
ARG UNAME=dev-user
ARG RAILS_ENV=development
RUN if [ "$RAILS_ENV" = "development" ] ; then \
        useradd --uid ${UID} --create-home --shell /bin/bash -G sudo,root ${UNAME} ; \
        UNAME=${UNAME} ; \
        echo "%${UNAME} ALL=(ALL:ALL) NOPASSWD: ALL" | sudo EDITOR='tee -a' visudo ; \
    fi
WORKDIR /workspace/myapp