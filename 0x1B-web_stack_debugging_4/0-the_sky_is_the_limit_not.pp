#higher limit
exec { 'higher limit' =
  command => "sed -i 's/15/4096' /etc/default/nginx",
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/sbin:/usr/local/bin',
}