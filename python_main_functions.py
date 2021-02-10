import sys, json, io, ancillary_functions

data = ancillary_functions.windows_friendly_json_converter(sys.argv[1])

notes = data["notes"]

tags_flattened = []
tags_final = []

for item in notes: 
    groups = item['groups']
    attachments = item['attachments']
    tag_collection = item['tags']
    if  groups: 
        for grouping in groups: 
            grouping.update({'description':  f"A group for {grouping['name']}s."})
    if attachments:
        for attachment in attachments: 
            attachment['id'] += 100000
    ancillary_functions.get_all_the_tags(tag_collection, tags_flattened)

ancillary_functions.remove_duplicates_and_flatten(tags_flattened, tags_final)

print("Behind the scenes, a new file, 'notes_fixed.json' is being written. In the meantime, here's the list of tags you requested")
print(tags_final)

note_object = {"notes" : notes}

ancillary_functions.make_a_json_file(note_object, 'notes_fixed.json')


