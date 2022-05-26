#!/usr/bin/python
import os
import shutil
import csv
import pandas as pd
from ansible.module_utils.basic import AnsibleModule

def main():

    module_args = dict(
        parameter_key=dict(default=None, type='list')
    )

    module = AnsibleModule(
        argument_spec=module_args
    )

    csv_filename = "/home/pi/Downloads/parameter/parameter.csv"

    df = pd.read_csv(csv_filename)
    
    for dic in module.params['parameter_key']:
        p_key = list(dic.keys())
        p_value = dic[p_key[0]]
        print(type(p_key[0]))
        for index, row in df.iterrows():
            if row['name'] == p_key[0]:
                df.loc[index, 'value'] = p_value
    
    df.to_csv(csv_filename, index=False)

    module.exit_json(changed=True,parameter_value=p_value)

if __name__ == '__main__':
    main()
