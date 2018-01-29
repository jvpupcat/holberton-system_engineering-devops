#higher limit
exec { 'higher limit':
  command => "sudo sed -i 's/15/4096' /etc/default/nginx; sudo service nginx restart",
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/sbin:/usr/local/bin',
}
