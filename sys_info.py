import click
from sys import byteorder, getdefaultencoding
from os import uname


def check_byte_order():
    click.echo('Byte order: \033[38;5;48m{}-endian\033[0m'.format(byteorder))


def check_operating_system():
    sys_info = uname()
    output_string = '''Name operating system: \033[38;5;48m{sys_name}\033[0m
Release: \033[38;5;48m{sys_release}\033[0m
Version: \033[38;5;48m{sys_version}\033[0m'''
    click.echo(output_string.format(sys_name=sys_info.sysname,
                                    sys_release=sys_info.release,
                                    sys_version=sys_info.version))


def check_file_system():
    click.echo('Encoding file system: \033[38;5;48m{}\033[0m'.format(getdefaultencoding()))


@click.command()
@click.option('-b', '--byte-order', help='Shows the byte order in the system',
              flag_value='byte-order')
@click.option('-o', '--operating-system',
              help='Shows information about operating system',
              flag_value='operating-system')
@click.option('-f', '--file-system', help='Shows information about file system encoding',
              flag_value='file-system')
def main(byte_order, operating_system, file_system):
    if byte_order is not None:
        check_byte_order()
    elif operating_system is not None:
        check_operating_system()
    elif file_system is not None:
        check_file_system()
    else:
        click.echo('Try flag --help for help')


if __name__ == '__main__':
    main()
