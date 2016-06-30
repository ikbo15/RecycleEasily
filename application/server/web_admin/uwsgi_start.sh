uwsgi 	--socket 127.0.0.1:8012 \
	--wsgi-file web_admin/wsgi.py \
	--processes 1 \
	--master \
	--pidfile /tmp/uwsgi_recycle_easily.pid \
	--vacuum \
	--daemonize /var/log/uwsgi/recycle_easily.loc



