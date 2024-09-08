#  Install and configure an Nginx server using Puppet

package {'nginx':
  ensure   => installed,
  provider => 'apt',
}

file {'/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  path    => '/etc/nginx/sites-available/default',
  mode    => '0766',
  require => Package['nginx'],
}

service {'nginx':
  ensure    => running,
  subscribe => Augeas['add__header'],
}
augeas { 'add__header':
  context => '/files/etc/nginx/sites-enabled/default',
  changes => [
    'ins add_header after server/server_name',
    'set server/add_header "X-Custom-Header $hostname always"',
  ],
  require => Package['nginx'],
  notify  => Service['nginx'],
}
