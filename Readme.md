# Python CLI: JSON CRUD


### Setting up the project folder
> python -m venv venv

### Activating the environment
> source venv/Scripts/activate

### Installing the dependencies
> pip install -r requirements.txt

### Running the application
> python cli.py

---
- [x] User listing:
  > python cli.py users
- [x] User search by ID:
  > python cli.py user 1
  - 1 is the ID of the user to search for.
- [x] User creation:
  > python cli.py new --name SomeName --lastname SomeLastname
  - --name and --lastname are required.
- [x] User deletion:
  > python cli.py delete 1
  - 1 is the ID of the user to be deleted.
- [] User modification
---

### Investigated sites
 - [Github Markdown - Sintaxis de escritura y formato básicos](https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)