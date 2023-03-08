#!/bin/sh

while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

#mysql -u root --password="$MYSQL_ROOT_PASSWORD"  << EOF
#USE ${MYSQL_DATABASE};
#GRANT ALL PRIVILEGES ON ${MYSQL_DATABASE}.* TO '${MYSQL_USER}';
#EOF

python manage.py migrate
python manage.py runserver 0.0.0.0:8000