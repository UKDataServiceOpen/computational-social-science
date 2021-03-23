## Download Republic of Ireland Register of Charities
## Diarmuid McDonnell
## 2020-05-27

# Import modules

import os # module for working with the operating system
import requests # module for requesting web pages


# Request file

file_webadd = "https://www.charitiesregulator.ie/media/1931/public-register-22052020.xlsx"
response_file = requests.get(file_webadd)


# Save files (data)

outfile = "ire-register-of-charities.xlsx"

if os.path.isfile(outfile): # do not overwrite existing file
    print("File already exists, no need to overwrite")
else: # file does not currently exist, therefore create
    with open(outfile, "wb") as f:
        f.write(response_file.content)

print("Finished executing script")        