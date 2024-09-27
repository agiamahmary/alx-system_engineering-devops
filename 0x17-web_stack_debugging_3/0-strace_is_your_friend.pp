#  Fix apache server error using Pnginx uppet

exec {'edit_wp_settings':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin'],
}
