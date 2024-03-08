#!/usr/bin/python3
"""Putting in servers"""
from os.path import exists, isdir
from fabric.api import run, put, env, local, sudo
from datetime import datetime
env.hosts = ['3.90.70.250', '52.87.230.58']
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_pack():
    """the function"""
    try:
        if isdir("versions") is False:
            local("mkdir versions")
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(current_date)
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """Deploiemnt"""
    if exists(archive_path) is False:
        return False
    try:
        sudo(put(archive_path, '/tmp/'))
        tmp_path = archive_path.split('/')[-1]
        path_rel = "/data/web_static/releases/"
        del_ext = tmp_path.split('.')[0]
        run(sudo('mkdir -p {}{del_ext}/'.format(path_rel)))
        sudo(
                run(
                    'tar -xzf /tmp/{} -C {}{}/'
                    .format(tmp_path, path_rel, del_ext)))
        run(sudo('rm /tmp/{}'.format(tmp_path)))
        run(sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path_rel, del_ext)))
        run(sudo('rm -rf {}{}/web_static'.format(path_rel, del_ext)))
        run(sudo('rm -rf /data/web_static/current'))
        run(
                sudo(
                    'ln -s {}{}/ /data/web_static/current'
                    .format(path_rel, del_ext)))
        return True
    except Exception as e:
        print(e)
        return False
