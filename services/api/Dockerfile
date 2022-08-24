FROM python:3.9.9-slim as python-base

# env variables
ENV POETRY_VERSION  "1.1.15"
ENV APP_WORK_PATH   "/app"
ENV PATH            "/root/.local/bin:$POETRY_HOME/bin:$PATH"

#########################
##     base builder     #
#########################
FROM python-base as builder-base

# install essentials
RUN apt-get update && \
    apt-get install -y \
    procps
RUN pip install -U pip
RUN pip install --user -q poetry==$POETRY_VERSION

# set working directory
WORKDIR $APP_WORK_PATH

# install app dependencies
COPY ./services/api/pyproject.toml  $APP_WORK_PATH
COPY ./services/api/poetry.lock     $APP_WORK_PATH
COPY ./packages                     $APP_WORK_PATH/packages

RUN poetry install

# copy app files
COPY ./services/api/ $APP_WORK_PATH


#########################
##     development     #
#########################
FROM python-base as development

# set working directory
WORKDIR $APP_WORK_PATH

# copy app files
COPY --from=builder-base  /root  /root
COPY --from=builder-base  $APP_WORK_PATH  $APP_WORK_PATH

# install dependencies
RUN poetry install

# expose app port
EXPOSE 5000

# start app
CMD poetry run python src/server.py