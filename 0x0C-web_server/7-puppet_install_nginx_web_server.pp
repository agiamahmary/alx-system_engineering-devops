#  Install and configure an Nginx server using Puppet

package {'nginx':
  ensure   => '1.4.6',
  provider => 'apt',
}

file {'/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => Package['nginx'],
}

service {'nginx':
  ensure    => running,
  provider  => 'service',
  subscribe => File['/etc/nginx/sites-enabled/default'],
}


augeas {'301 Moved Permanently':
  context => '/etc/nginx/sites-enabled/default',
  changes => [
    'SET /server[1]/location[last()+1]/path "/redirect_me"',
    'SET /server[1]/location[last()+1]/return "301 "https://youtu.be/B9LYL5OO7eQ?si=Z0UqqX7R97tM-7Gi',
  ],
  require => Package['nginx'],
  notify  => Service['nginx'],
}
