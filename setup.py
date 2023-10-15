#!/usr/bin/env python3
#
#
#       Copyright 2023 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import src.commons.common_functions as cf


if __name__ == '__main__':
    # Add Banner
    cf.print_mega_banner(cf.get_file_name(sys.argv[0], True))
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
