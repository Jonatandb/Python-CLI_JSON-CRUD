import click
import json_manager

@click.group()
def cli():
    pass

@cli.command()
def users():
    users = json_manager.read_json()
    print('Id\tName\t\tLastname')
    for user in users:
        print( f"{user['id']}\t{user['name']}\t{user['lastname']}")

if __name__ == '__main__':
    cli()
