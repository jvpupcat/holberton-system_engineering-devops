file { '/tmp/holberton':
        ensure  => 'present',
        owner   => 'www-data',
        group   => 'www-data',
        mode    => 744,
        content => "I love Puppet"
}
