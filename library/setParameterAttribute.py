#!/usr/bin/python
import os
import shutil
import pandas as pd
from ansible.module_utils.basic import AnsibleModule

def main():

    module_args = dict(
            name=dict(required=True, type='str'),
            parent=dict(type='str'),
            notification=dict(type='int'),
            notification_change=dict(required=True, type='bool'),
            accesslist=dict(type='list'),
            accesslist_change=dict(required=True, type='bool')
    )

    module = AnsibleModule(
        argument_spec=module_args
    )

    if module.params['notification'] > 2 or module.params['notification'] < 0:
        module.fail_json(msg="notification value can only be set to 0 ,1 or 2")
    else: 
        csv_filename = "parameter.csv"

        df = pd.read_csv(csv_filename)
        
        for index, row in df.iterrows():
            if row['name'] == module.params['name']:
                if module.params['notification_change']:
                    df.loc[index, 'notification'] = module.params['notification']
                if module.params['accesslist_change']:
                    df.loc[index, 'accesslist'] = module.params['accesslist']

        df.to_csv(csv_filename, index=False)

        module.exit_json(changed=True)

if __name__ == '__main__':
    main()
