#!/bin/bash

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Error: docker-compose is not installed.' >&2
  exit 1
fi

domains=(d9-test-server.q6z4kzhr.uk)
rsa_key_size=4096
data_path="./nginx/certbot"
email="d9network2019@gmail.com" # 为了接收重要通知而填写（例如证书到期通知）
staging=0 # 如果是测试，设置为1

if [ -d "$data_path" ]; then
  read -p "Existing data found for $domains. Continue and replace existing certificate? (y/N) " decision
  if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
    exit
  fi
fi

mkdir -p "$data_path/conf"
mkdir -p "$data_path/www"

docker-compose run --rm --entrypoint "\
  sh -c 'chmod 755 /var/www/certbot && certbot certonly --webroot -w /var/www/certbot \
  -d ${domains[*]} \
  --email $email \
  --rsa-key-size $rsa_key_size \
  --agree-tos \
  --force-renewal \
  ${staging:+--staging}'" certbot
