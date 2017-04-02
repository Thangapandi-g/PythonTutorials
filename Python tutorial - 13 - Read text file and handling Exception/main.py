import sys
import pprint
try:
    file_content = open("input.txt")
    each_line = file_content.readline().strip()
    pprint.pprint("each_line = "+each_line)
    convert_to_int = int(each_line)
    pprint.pprint(convert_to_int)
except ValueError as value_error:
    print("Cannot convert to int. Detail error = {0}".format(value_error))
except OSError as os_error:
    print("OS Error detail = {0}".format(os_error))
except:
    print("Unexpected error : ", sys.exc_info()[0])
    raise
