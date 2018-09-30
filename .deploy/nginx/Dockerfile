############################################
# Docker Image
#  - https://github.com/nginxinc/docker-nginx/blob/d377983a14b214fcae4b8e34357761282aca788f/stable/alpine/Dockerfile
############################################
FROM nginx:1.14.0-alpine

# awsにデプロイする時はecs taskの環境変数で上書きして設定ファイルを書き換える
ENV APP_HOST 127.0.0.1
ENV APP_PORT 5000

# nginxの設置ファイルを書き換える為のテンプレートエンジン
RUN apk --no-cache add gettext curl
RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf /tmp/default.conf.template
#COPY ./localhost-status.conf /etc/nginx/conf.d/localhost-status.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./startup.sh /shell/startup.sh
RUN chmod +x /shell/startup.sh

CMD ["/bin/sh", "/shell/startup.sh"]
