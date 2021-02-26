https://tri-amdd.github.io/beep/tutorial/
https://www.sciencedirect.com/science/article/pii/S2352711020300492


export BEEP_ENV="dev"
export BEEP_PROCESSING_DIR="tutorial"

# Ran tutorial and got terminal output

'''
python battery_cycler_data.py 
/home/nbosio1001/anaconda3/lib/python3.7/site-packages/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.25.11) or chardet (3.0.4) doesn't match a supported version!
  RequestsDependencyWarning)
Beginning file download with requests
100%|█████████████████████████████████████████████| 2/2 [00:02<00:00,  1.10s/it]
--- Logging error ---
Traceback (most recent call last):
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 1025, in emit
    msg = self.format(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 869, in format
    return fmt.format(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 611, in format
    s = self.formatMessage(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 580, in formatMessage
    return self._style.format(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 422, in format
    return self._fmt % record.__dict__
KeyError: 'service'
Call stack:
  File "battery_cycler_data.py", line 50, in <module>
    validated = validate.validate_file_list_from_json(mapped)
  File "/home/nbosio1001/anaconda3/lib/python3.7/site-packages/beep/validate.py", line 638, in validate_file_list_from_json
    logger.warning("{file_list_size} files being validated, should be 1")
Message: '{file_list_size} files being validated, should be 1'
Arguments: ()
100%|█████████████████████████████████████████| 877/877 [01:10<00:00, 12.45it/s]
100%|█████████████████████████████████████████| 877/877 [01:15<00:00, 11.67it/s]
100%|█████████████████████████████████████████| 877/877 [01:12<00:00, 12.05it/s]
100%|█████████████████████████████████████████| 877/877 [01:13<00:00, 11.87it/s]
--- Logging error ---
Traceback (most recent call last):
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 1025, in emit
    msg = self.format(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 869, in format
    return fmt.format(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 611, in format
    s = self.formatMessage(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 580, in formatMessage
    return self._style.format(record)
  File "/home/nbosio1001/anaconda3/lib/python3.7/logging/__init__.py", line 422, in format
    return self._fmt % record.__dict__
KeyError: 'service'
Call stack:
  File "battery_cycler_data.py", line 59, in <module>
    structured = structure.process_file_list_from_json(validated)
  File "/home/nbosio1001/anaconda3/lib/python3.7/site-packages/beep/structure.py", line 2202, in process_file_list_from_json
    logger.warning("{file_list_size} files being validated, should be 1")
Message: '{file_list_size} files being validated, should be 1'
Arguments: ()
4.6974263191223145
876
1.1737735271453857
1.1737735271453857
'''
  
