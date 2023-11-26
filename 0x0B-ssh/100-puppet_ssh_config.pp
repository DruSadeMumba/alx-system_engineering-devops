# Puppet manifest for SSH client configuration

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path => '/etc/ssh/sshd_config',
  line => 'IdentityFile ~/.ssh/school',
}
