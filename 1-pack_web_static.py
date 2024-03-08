#!/usr/bin/python3
"""Archiving"""
from datetime import datetime
from fabric.api import local
from os.path import exists, isdir


def do_pack():
    """the function"""
    try:
        if exists("versions") is False or isdir("versions") is False:
            local("mkdir versions")
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"versions/web_static_{current_date}.tgz"
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception:
        return None
