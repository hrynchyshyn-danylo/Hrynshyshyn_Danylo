import os


# before all and after all
def before_all(context):
    if os.path.exists(context.config.userdata.get('path_local_file_created')):
        os.remove(context.config.userdata.get('path_local_file_created'))
    if os.path.exists(context.config.userdata.get('path_local_file_downloaded')):
        os.remove(context.config.userdata.get('path_local_file_downloaded'))

def after_all(context):
    if os.path.exists(context.config.userdata.get('path_local_file_created')):
        os.remove(context.config.userdata.get('path_local_file_created'))
    if os.path.exists(context.config.userdata.get('path_local_file_downloaded')):
        os.remove(context.config.userdata.get('path_local_file_downloaded'))