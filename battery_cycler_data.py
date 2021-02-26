import os
import requests


print('Beginning file download with requests')

# def __init__(self):
data_dir = './Severson-et-al/'

# class DownloadFiles:
#     try:
#         os.makedirs(data_dir)
#     except FileExistsError:
#         pass

#     url = 'https://data.matr.io/1/api/v1/file/5c86c0bafa2ede00015ddf70/download'
#     r = requests.get(url)

#     with open(os.path.join(data_dir, '2017-05-12_6C-50per_3_6C_CH36.csv'), 'wb') as f:
#         f.write(r.content)

#     url = 'https://data.matr.io/1/api/v1/file/5c86c0b5fa2ede00015ddf6d/download'
#     r = requests.get(url)

#     with open(os.path.join(data_dir, '2017-05-12_6C-50per_3_6C_CH36_Metadata.csv'), 'wb') as f:
#         f.write(r.content)

#     # Retrieve HTTP meta-data
#     print("Status code", r.status_code)
#     print("File type recieved", r.headers['content-type'])
#     print("File encoding", r.encoding)

import json
import glob

# Import beep scripts
from beep import validate, structure, featurize


file_list = glob.glob(os.path.join(data_dir, '*[0-9].csv'))

mode = 'events_off'
mapped  =  {
            "mode": 'events_off',  # mode run|test|events_off
            "file_list": file_list,  # list of file paths ['path/test1.csv', 'path/test2.csv']
            'run_list': list(range(len(file_list)))  # list of run_ids [0, 1]
            }
mapped = json.dumps(mapped)
# class Validation:
validated = validate.validate_file_list_from_json(mapped)
validated_output = json.loads(validated)
validated_output['mode'] = mode  # mode run|test|events_off
validated_output['run_list'] = list(range(len(validated_output['file_list'])))
validated = json.dumps(validated_output)

# print(validated)

# class Data_structuring:
structured = structure.process_file_list_from_json(validated)
structured_output = json.loads(structured)
structured_output['mode'] = mode  # mode run|test|events_off
structured_output['run_list'] = list(range(len(file_list)))
structured = json.dumps(structured_output)

    # print(structured)

# class Featurization:
featurized = featurize.process_file_list_from_json(structured)
featurized_output = json.loads(featurized)
featurized_output['mode'] = mode  # mode run|test|events_off
featurized_output['run_list'] = list(range(len(file_list)))
featurized = json.dumps(featurized_output)

from matplotlib import pyplot as plt
from monty.serialization import loadfn
# class Interpolation:
processing_dir = os.environ.get("BEEP_PROCESSING_DIR", "tutorial")
struct = loadfn(os.path.join(processing_dir, 'data-share', 'structure', '2017-05-12_6C-50per_3_6C_CH36_structure.json'))
reg_charge = struct.cycles_interpolated[struct.cycles_interpolated.step_type == 'charge']
print(reg_charge.current[reg_charge.cycle_index == 25].mean())
print(reg_charge.cycle_index.max())
print(reg_charge.charge_capacity[reg_charge.cycle_index == 25].max())
print(reg_charge.charge_capacity[reg_charge.cycle_index == 600].max())
plt.plot(reg_charge.charge_capacity[reg_charge.cycle_index == 600], reg_charge.voltage[reg_charge.cycle_index == 600])
plt.show()
