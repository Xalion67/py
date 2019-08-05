from random import randint
import pyperclip as buffer
import click


@click.command()
@click.option('--len', '-l', help='Password length',
              prompt='Enter password length')
def generate_password(len):
    # Раскрашиваем вывод в зелёный
    GREEN = '\033[38;5;48m'
    END_GREEN = '\033[0m'

    password = ''
    for i in range(int(len)):
        password += chr(randint(33, 126))

    click.echo('Your password: ' + GREEN + password)

    # Копируем пароль в буфер обмена
    buffer.copy(password)
    click.echo('Password copied to clipboard' + END_GREEN + '\n')


if __name__ == '__main__':
    generate_password()
