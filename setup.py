import sys
import src.commons.common_functions as cf


if __name__ == '__main__':
    # Show script info
    info = {
        "name": str(cf.get_file_name(sys.argv[0], True)),
        "location": sys.argv[0],
        "description": "Basic Python3 template",
        "Autor": "Alejandro Gómez",
        "calling": "{0} parameters".format(sys.argv[0])
    }
    cf.show_script_info(info)

    # info menssage
    cf.info_msg("info menssage")
