# typo fix in wp-settings.php
exec { 'replace phpp with php':
	command => sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
	path 	=> ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
}
