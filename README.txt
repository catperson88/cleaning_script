Welcome to the MackeyRMS Coding Challenge. 
Below are the guidelines for this challenge.


In this package you will find:
* README.txt  - this file
* notes_sample.json  - the example json file for this challenge.


GOAL:
Your script when run, should read in the notes_sample.json and execute some changes to the data set as described below. 
The modified data set should then be output to a new file called notes_fixed.json

The script can be coded in any language of choice.  (i.e. Python, PHP, Ruby, JavaScript, Java)
It must be able to be run on the command line of any Mac/Windows/Linux laptop/desktop.



1.  Add Item to all Group objects.

Within in a note object there exists an item called "groups" which contain a list of group objects.
ie.    {
          "name": "Micro Cap",
          "id": 15
        }

Please add an additional item to this object called "description" such that it appears as follows:

       The attached file contains JSON data which needs to be cleaned given the following rules.
       {
          "name": "Micro Cap",
          "id": 15,
	  "description": "A group for Micro Caps"
        }

The change should be made to all group object items in the data set. 


2.  Substitute all File Ids instances.
We need to change all file ids such that the id value is 100000 more than the current value.
This only applies to "attachments" list  which are listed in the "attachments" item for each note object. 

Example:  

BEFORE:
	{
          "matches_search": null,
          "bytesize": 1,
          "html_preview": "<img src=\"/files/2157/preview/preview.png\"/><br/>\n",
          "content_type": "application/octet-stream",
          "previews": [
            "/files/2157/preview/preview.png"
          ],
          "id": 2157,
          "filename": "Financial Model (4).xls"
        }

AFTER
	{
          "matches_search": null,
          "bytesize": 1,
          "html_preview": "<img src=\"/files/102157/preview/preview.png\"/><br/>\n",
          "content_type": "application/octet-stream",
          "previews": [
            "/files/102157/preview/preview.png"
          ],
          "id": 102157,
          "filename": "Financial Model (4).xls"
        }



NOTE: all file ids are found within the following attributes within the attachments list: html_preview, previews and id.  
See example above. 


3.  Write the updated data structure in JSON back to a file.

4.  Output to the screen, the distinct list of tags .  A list of tags exist for each note object. 

Sample output:


i.e. 

>  python3 fix_json.py notes_sample.json
(behind the scenes a new file , notes_fixed.json is being written)


AAPL US
EBAY US
NFLX US

NOTE:  The output should not have any repeating tags/values.


