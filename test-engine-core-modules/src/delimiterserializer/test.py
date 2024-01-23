import csv

from test_engine_core.interfaces.iserializer import ISerializer
from test_engine_core.plugins.enums.delimiter_type import DelimiterType
from test_engine_core.plugins.enums.plugin_type import PluginType
from test_engine_core.plugins.enums.serializer_plugin_type import SerializerPluginType
from test_engine_core.plugins.metadata.delimiter_metadata import DelimiterMetadata
from test_engine_core.plugins.metadata.plugin_metadata import PluginMetadata

data_path = "user_defined_files/sv_tab.csv"
supported_separated_values_list = [
    (DelimiterType.COMMA, ","),
    (DelimiterType.TAB, "\t"),
    (DelimiterType.SEMICOLON, ";"),
    (DelimiterType.PIPE, "|"),
    (DelimiterType.SPACE, " "),
    (DelimiterType.COLON, ":"),
]

    
with open(data_path, "r") as text_file:
    list_data = list(csv.reader(text_file))
print(list_data)
# check if SV file only has a single column by checking for presence of supported SVs
# if comma, this will run

if all(
    supported_separated_value[1] not in list_data[0][0]
    for supported_separated_value in supported_separated_values_list
):
    delimiter_tuple = (DelimiterType.COMMA, ",")
    delimiter_instance = DelimiterMetadata(
        list_data, delimiter_tuple, data_path
    )
    # return delimiter_instance
        
else:
    with open(data_path, 'r') as file:
        content = file.read()
        dialect = csv.Sniffer().sniff(content)
        detected_delimiter_tuple = None
        for count, item in enumerate(supported_separated_values_list):
            print(supported_separated_values_list[count][1])
            if (
                dialect.delimiter
                == supported_separated_values_list[count][1]
            ):
                detected_delimiter_tuple = item
                break

        # if delimiter is not found in our list of supported delimiters
        if not detected_delimiter_tuple:
            raise ValueError("The delimiter is not supported.")


        file.seek(0)
        reader = csv.reader(file, delimiter=dialect.delimiter)
        list_data_with_delimiter = list(reader)
        print(list_data_with_delimiter)
        print(dialect.delimiter)
        delimiter_instance = DelimiterMetadata(
            list_data_with_delimiter, detected_delimiter_tuple, data_path
        )
    #     return delimiter_instance