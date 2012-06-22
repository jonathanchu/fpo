import os
from fabric.api import local, env, settings, run, cd, sudo

env.project_dir = os.getcwd()

#env.hosts = ['']

env.static_path = './website/static'
env.sass_bin = 'sass'
env.yui_bin = 'java -jar ./project_files/yuicompressor.jar'

def sass_watch():
    local('sass --scss --watch website/static/css-src/base.scss:website/static/gen/css/site.css')

def bootstrap():
    #http://yui.zenfs.com/releases/yuicompressor/yuicompressor-2.4.7.zip
    pass

def test():
    local('python website/tests/test_views.py')
    pass
