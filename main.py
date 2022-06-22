import typer
import week5.multithread_program
import week7.multithread_program_final

app = typer.Typer()
app.add_typer(week5.multithread_program.app, name="week5")
app.add_typer(week7.multithread_program_final.app, name="week7")

@app.command()
def hello(name:str):
    typer.echo(f"Hello, {name}")

@app.command()
def goodbye(name: str):
    typer.echo(f"Bye {name}!")


if __name__ == '__main__':
    app()