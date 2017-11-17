# script that creates a manifest that kills a process

exec { 'killmenow':
  command => 'pkill -f ./killmenow',
  cwd => '/root',
  provider => 'shell'
}
