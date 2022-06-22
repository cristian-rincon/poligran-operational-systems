import os
from typing import List, Optional

import typer
import threading
from queue import Queue

app = typer.Typer()

BANNER = """
███    ███ ██    ██ ██      ████████ ██ ████████ ██   ██ ██████  ███████  █████  ██████  
████  ████ ██    ██ ██         ██    ██    ██    ██   ██ ██   ██ ██      ██   ██ ██   ██ 
██ ████ ██ ██    ██ ██         ██    ██    ██    ███████ ██████  █████   ███████ ██   ██ 
██  ██  ██ ██    ██ ██         ██    ██    ██    ██   ██ ██   ██ ██      ██   ██ ██   ██ 
██      ██  ██████  ███████    ██    ██    ██    ██   ██ ██   ██ ███████ ██   ██ ██████  
                                                                                         
                                                                                         
██████  ██████   ██████   ██████  ██████   █████  ███    ███                             
██   ██ ██   ██ ██    ██ ██       ██   ██ ██   ██ ████  ████                             
██████  ██████  ██    ██ ██   ███ ██████  ███████ ██ ████ ██                             
██      ██   ██ ██    ██ ██    ██ ██   ██ ██   ██ ██  ██  ██                             
██      ██   ██  ██████   ██████  ██   ██ ██   ██ ██      ██                             
                                                                                         
                                                                                         
"""


PROMPTS = [
    "Is the thread empty? (True/False)",
    "Thread 1 is empty",
    "Thread 1 is not empty",
    "Thread 1 is created",
    "Thread 2 is created",
    "Thread 1 is started",
    "Thread 2 is started",
]



def clean():
    """Clean the threads, and terminate the program"""
    typer.secho("Cleaning threads", fg="yellow")
    os._exit(0)
    

def generate(empty, queue):
    """Generate new thread with a variable called empty, with value True."""
    queue.put(empty)

def consume(empty, queue):
    """Consume the thread with a variable called empty, with value False."""

    data = queue.get()
    if data:
        typer.secho(PROMPTS[1], fg="red")
    else:
        typer.secho(PROMPTS[2], fg="green")
        typer.secho(f"Received data from thread 1, into thread 2: {data}", fg="blue")
        clean()

@app.command(
    name="program",
    help="A program that creates threads and prints the status of the thread."
)
def main():
    """Main function"""
    queue = Queue()
    typer.secho(BANNER, fg="green")
    typer.secho(
        """
        This program creates two threads, asks if thread 1 is empty, 
        and if this statement is true, will wait with that value, 
        if the statement is false, will share that information with thread 2
        \n""", fg="yellow")
    empty = typer.prompt(PROMPTS[0], default=True)
    # While the thread is empty, print the status of the thread, if the thread is not empty
    # Initialize thread 1

    while empty:
        typer.secho(PROMPTS[1], fg="red")
        empty = typer.prompt(PROMPTS[0], default=True)

    thread1 = threading.Thread(target=generate, args=(empty, queue))
    typer.secho(PROMPTS[3], fg="green")
    thread2 = threading.Thread(target=consume, args=(empty, queue))
    typer.secho(PROMPTS[4], fg="green")
    thread1.start()
    thread2.start()
    queue.join()


if __name__ == '__main__':
    app()