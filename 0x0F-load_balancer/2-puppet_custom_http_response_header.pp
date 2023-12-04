# Add a custom HTTP header with Puppet

package { 'nginx':
  ensure => installed,
  before   => Exec['header'],
}

exec { 'header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\theader X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
