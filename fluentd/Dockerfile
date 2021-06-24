FROM fluent/fluentd:v1.13-1

USER root
RUN mkdir -p ./logs

COPY fluent.conf /fluentd/etc/

USER fluent