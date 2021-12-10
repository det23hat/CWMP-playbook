#!/usr/bin/python
import os
import shutil
import pandas as pd
from ansible.module_utils.basic import AnsibleModule

def main():

    module_args = dict(
        name=dict(required=True, type='list')
    )

    module = AnsibleModule(
        argument_spec=module_args
    )

    param_list = module.params['name']

    ParameterList = []

    csv_filename = "parameter.csv"

    df = pd.read_csv(csv_filename)

    for param_name in param_list:
        for index, row in df.iterrows():
            if row['name'] == param_name:
                ParameterAttributeStruct = {}
                ParameterAttributeStruct['Name'] = param_name
                ParameterAttributeStruct['Value'] = row['value']
                break
        ParameterList.append(ParameterAttributeStruct)

        

    module.exit_json(changed=False,ParameterList=ParameterList)

if __name__ == '__main__':
    main()

