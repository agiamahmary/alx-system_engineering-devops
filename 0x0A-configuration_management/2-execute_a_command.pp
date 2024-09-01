# Using Puppet, create a manifest that kills a process named killmenow.

exec {'killmenow':
  command => 'pkill -f killmenow',
  cwd     => '/root/maryagiamah/alx-system_engineering-devops/0x0A-configuration_management',
  path    => '/usr/bin/',
}
