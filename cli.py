import click
import json_manager


@click.group()
def cli():
    """ Python CLI JSON CRUD made by Jonatandb@gmail.com, supported by Click. """
    pass


@cli.command()
@click.option("--name", required=True, help="Name of the user")
@click.option("--lastname", required=True, help="Lastname of the user")
@click.pass_context
def new(ctx, name, lastname):
    if not name or not lastname:
        ctx.fail("name and lastname are required")
    else:
        users = json_manager.read_json()
        new_id = len(users) + 1
        new_user = {"id": new_id, "name": name, "lastname": lastname}
        users.append(new_user)
        json_manager.write_json(users)
        print(f"User {name} {lastname} created successfully with id {new_id}")


@cli.command()
def users():
    users = json_manager.read_json()
    if users:
        for user in users:
            print(f"{user['id']} - {user['name']} - {user['lastname']}")
    else:
        print("No users")


@cli.command()
@click.argument('id', type=int)
def user(id):
    users = json_manager.read_json()
    user = next((user for user in users if user['id'] == id), None)
    if not user:
        print(f"User with id {id} not found")
    else:
        print(f"{user['id']} - {user['name']} - {user['lastname']}")


@cli.command()
@click.argument('id', type=int)
def delete(id):
    users = json_manager.read_json()
    user = next((user for user in users if user['id'] == id), None)
    if not user:
        print(f"User with id {id} not found")
    else:
        users.remove(user)
        json_manager.write_json(users)
        print(f"User with id {id} deleted successfully")


@cli.command()
@click.argument('id', type=int)
@click.option("--name", help="Name of the user")
@click.option("--lastname", help="Lastname of the user")
def update(id, name, lastname):
    users = json_manager.read_json()
    user = next((user for user in users if user['id'] == id), None)
    if not user:
        print(f"User with id {id} not found")
    else:
        if name is not None:
            user['name'] = name
        if lastname is not None:
            user['lastname'] = lastname
        json_manager.write_json(users)
        print(f"User with id {id} updated successfully")


if __name__ == "__main__":
    cli()
