# Define an exec resource to run the fix command
exec { 'fix_apache_issue':
  command  => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  provider => shell,
}
