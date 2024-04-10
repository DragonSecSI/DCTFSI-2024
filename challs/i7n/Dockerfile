FROM php:8-apache

ARG FLAG=dctf{fake_flag}

# Enable .htaccess
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

COPY chall/ .

# Include the flag
RUN cat > ./media/flag.txt <<EOF
FLAG=${FLAG}
EOF

# Allow uploads
RUN chmod 777 ./media -R && chmod 777 ./users -R
