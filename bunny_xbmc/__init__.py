import sys
import os
from shutil import copytree, ignore_patterns


def bunny_repo():
    print "Creating repo for deploiment..."


def bunny_crate():
    if sys.argv.__len__() < 3:
        print "\033[91m Specefy type and appname please. Example: 'bunny_create video helloworld'. For more infor use help \033[0m"
        return

    app_type = sys.argv[1]
    app_name = sys.argv[2]
    app_id = 'script.%s.%s' % (app_type, app_name)
    current_folder = os.getcwd()

    source = os.path.join(os.path.dirname(__file__), 'workflow/')

    destination = os.path.join(current_folder, app_id + '/')

    copytree(source, destination, ignore=ignore_patterns('*.pyc',))

    for fl in os.listdir(destination):
        if '.tmplt' in fl:
            with open(os.path.join(destination, fl), 'rw') as f:
                content = f.read()
                rendered_content = content.format(name=app_name, type=app_type)
                new_f = open(os.path.join(destination, fl.replace('.tmplt', '')), 'w+')
                new_f.write(rendered_content)
                new_f.close()
            os.remove(os.path.join(destination, fl))
