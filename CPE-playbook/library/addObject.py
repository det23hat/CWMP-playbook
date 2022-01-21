#!/usr/bin/python
import os
import shutil
import pickle
from ansible.module_utils.basic import AnsibleModule

class CwmpObject:
    def __init__(self, name, writable, parent, parameter_key):
        self.name = name
        self.writable = writable
        self.parent = parent
        self.parameter_key = parameter_key


def main():

    module_args = dict(
            writable=dict(default=True, type='bool'),
            parameter_key=dict(default=None, type='list'),
            parent=dict(required=True, type='str')
    )

    module = AnsibleModule(
        argument_spec=module_args
    )

    parameter_dict={}
    param_object_list=[]

    
    for key in module.params['parameter_key']:
        parameter_dict.update(key)

    instance_path = "cwmpInstance.txt"
    instance_num = 1
    cwmp_object_list = []
    parent = module.params['parent']

    f = open(instance_path, "rb+")

    if os.stat(instance_path).st_size == 0 :
        name = parent + '/1'
    else:
        while True:
            try:
                host_instance = pickle.load(f)
                if host_instance.parent == parent :
                    instance_num += 1 
                    cwmp_object_list.append(host_instance)
            except EOFError:
                break
    name = module.params['parent']+ '/{instance_num}'
    newObject = CwmpObject(name,module.params['writable'],module.params['parent'],parameter_dict)
    cwmp_object_list.append(newObject)

    pickle.dump(newObject,f)


    f.close()
    
    module.exit_json(changed=False,set_value=parameter_dict,instanceNum=instance_num,host=host_instance.parent)

if __name__ == '__main__':
    main()
