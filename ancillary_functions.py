import sys, json, io

def windows_friendly_json_converter(json_file):
    f = io.open(json_file, encoding="utf-8")
    return json.load(f)

def get_all_the_tags(tag_list, target_list):
    if len(tag_list) > 1:
        for tag in tag_list:
            target_list.append([tag])
    else:
        target_list.append(tag_list)


def remove_duplicates_and_flatten(array1, array2):
    for item1 in array1:
        for item2 in item1:
            if item2 not in array2:
                array2.append(item2)


def make_a_json_file(data_to_convert, json_file_name="remember_to_name_your_file_next_time.json"):
    with open(json_file_name, 'w') as f:
        return json.dump(data_to_convert, f)
