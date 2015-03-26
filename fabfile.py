from fabric import api

api.env.hosts = [
    'root@174.140.227.137',
]

@api.task
def deploy():
    with api.cd('/root/deploy-test'):
        api.sudo('git pull',user='root')
    

