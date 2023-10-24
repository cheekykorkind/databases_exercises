FROM ruby:3.2.2-slim

RUN apt update && apt install -y unzip curl gnupg libpq-dev sudo git make tzdata cron cronutils g++ imagemagick vim gnupg2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# nodejs를 위한 asdf 인스톨
ARG asdf_dir=/opt/asdf
ARG asdf_version=0.13.1
ENV ASDF_DIR=${asdf_dir} \
    ASDF_DATA_DIR=${asdf_dir} \
    PATH=${asdf_dir}/bin:${asdf_dir}/shims:${PATH}
RUN mkdir -p ${asdf_dir} \
    && git clone https://github.com/asdf-vm/asdf.git ${asdf_dir} --branch v${asdf_version} \
    && asdf plugin add nodejs \
    && asdf install nodejs 20.8.1 \
    && asdf global nodejs 20.8.1

ARG USER_UID=1001
ARG USER_GID=1001
ARG UNAME=dev-user
ARG RAILS_ENV=development
ENV UID ${USER_UID}
ENV GID ${USER_GID}
ENV UNAME ${UNAME}
ENV RAILS_ENV ${RAILS_ENV}
RUN if [ "$RAILS_ENV" = "development" ] ; then \
	    groupadd -g $GID nopass ; \
        useradd --uid $UID --create-home --shell /bin/bash -G sudo,root,nopass $UNAME ; \
        echo '%nopass ALL=(ALL:ALL) NOPASSWD: ALL' | sudo EDITOR='tee -a' visudo ; \
    fi
WORKDIR /workspace/myapp