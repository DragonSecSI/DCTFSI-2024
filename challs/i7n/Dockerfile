FROM php:8-apache

RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

COPY chall/ .

RUN cat > ./media/flag.txt <<EOF
FLAG=dctf{formerly_known_as_x}
EOF

RUN chmod 777 ./media -R && chmod 777 ./users -R
