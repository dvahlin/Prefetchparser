# Prefetchparser
Parser for Windows10/11 Prefetch files

Using libscca (https://github.com/libyal/libscca)

Script to parse output from pyscca

Work in progress

With PIP
* pip install libscca-python

Install libscca:
* Download tar file from https://github.com/libyal/libscca/releases
* Unpack with tar xvf <file>
* run command: python3 setup.py install


### Example usage and output

```
┌──(user㉿computer)-[~/prefetch]
└─$ python3 parse.py -i Prefetch/POWERSHELL.EXE-59FC8F3D.pf
EXECUTABLE NAME:        POWERSHELL.EXE 
RUN COUNT:      26 
LAST EXECUTED:  2023-08-08 21:00:21.801815


HISTORY:
Run 1:  2023-08-08 21:00:21.801815
Run 2:  2023-08-08 20:44:44.421291
Run 3:  2023-08-08 20:41:01.438052
Run 4:  2023-08-08 20:14:10.854393
Run 5:  2023-08-09 04:35:57.208765
Run 6:  2023-08-08 05:26:15.977499
Run 7:  2023-08-08 05:26:15.143587
Run 8:  2023-08-08 05:26:05.973647
```



Dependencies identified: python3-dev python3-setuptools


