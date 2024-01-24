# User limit

exec {'replac':
  provider => shell,
  command  => 'sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['replace'],
}

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}