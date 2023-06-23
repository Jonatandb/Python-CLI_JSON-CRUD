import click
import json_manager


@click.group()
def cli():
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


if __name__ == "__main__":
    cli()
