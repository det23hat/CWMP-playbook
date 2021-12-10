#!/usr/bin/python
import os
import shutil
import pickle
from ansible.module_utils.basic import AnsibleModule

def main():

    module_args = dict(
            instance_num=dict(required=True, type='int'),
            parent=dict(required=True, type='str')
    )

    module = AnsibleModule(
        argument_spec=module_args
    )

    instance_path = "cwmpInstance.txt"
    cwmp_object_list = []
    name = module.params['parent']+'/'+{module.params['instance_num']}
    
    f = open(instance_path, "rb+")

    while True:
        try:
            host_instance = pickle.load(f)
            if host_instance.name != name :
                cwmp_object_list.append(host_instance)
        except EOFError:
            break
    
    f.seek(0)
    f.truncate()

    for i in range(len(cwmp_object_list)):
        pickle.dump(cwmp_object_list[i], f)
    else:
        f.close()

    module.exit_json(changed=True,msg="Has deleted Object {name}")

if __name__ == '__main__':
    main()