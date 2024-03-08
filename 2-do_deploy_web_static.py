#!/usr/bin/python3
"""Putting in servers"""
from os.path import exists
from fabric.api import run, put, env
env.hosts = ['3.90.70.250', '52.87.230.58']

def do_deploy(archive_path):
    """Deploiemnt"""
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        tmp_path = archive_path.split('/')[-1]
        path_rel = "/data/web_static/releases/"
        del_ext = tmp_path.split('.')[0]
        run(f'mkdir -p {path_rel}{del_ext}/')
        run('tar -xzf /tmp/{} -C {}{}/'.format(tmp_path, path_rel, del_ext))
        run(f'rm /tmp/{tmp_path}')
        # run('mv {0}{1}/web_static/* {0}{1}/'.format(path_rel, del_ext))
        # run('rm -rf {}{}/web_static'.format(path_rel, del_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path_rel, del_ext))
        return True
    except Exception:
        return False
