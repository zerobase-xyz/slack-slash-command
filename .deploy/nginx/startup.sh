#!/bin/sh

# nginxのserver_nameとfastcgit_passを書き換える
envsubst '$$APP_HOST$$APP_PORT' \
        < /tmp/default.conf.template \
        > /etc/nginx/conf.d/default.conf

# nginxのフォアグランドで起動する
nginx -g "daemon off;"
