import typer
import week5.multithread_program

app = typer.Typer()
app.add_typer(week5.multithread_program.app, name="multithread_program")

@app.command()
def hello(name:str):
    typer.echo(f"Hello, {name}")

@app.command()
def goodbye(name: str):
    typer.echo(f"Bye {name}!")


if __name__ == '__main__':
    app()