from typing import Optional
import typer
import random
import time

## An alternative CLI argument declaration (MANDATORY)
"""def main(name: str = typer.Argument(...)):
    typer.echo(f"Hello {name}")"""

## Make an optional CLI argument
"""def main(name: Optional[str] = typer.Argument(None)):
    if name is None:
        typer.echo("Hello World!")
    else:
        typer.echo(f"Hello {name}")"""

## Argument with default and with help
"""def get_name():
    return random.choice(["Deadpool", "Rick", "Morty", "Hiro"])
def main(name: str = typer.Argument(..., help="Give your name"), lastname: str = typer.Argument(get_name)):
    typer.echo(f"Hello {name} {lastname}")"""

## WITH ENV VARIABLE (export AWESOME_NAME=toto)
"""def main(name: str = typer.Argument("World", envvar=["AWESOME_NAME", "GOD_NAME"])):
    typer.echo(f"Hello Mr. {name}")"""

## OPTION
"""def main(fullname: str = typer.Option("Wade Wilson", show_default=True, help="Option name")):
    typer.echo(f"Hello {fullname}")"""

## REQUIRE OPTION
"""def main(name: str, lastname: str = typer.Option(...)):
    typer.echo(f"Hello {name} {lastname}")"""

## OPTION WITH PROMPT
"""def main(name: str, lastname: str = typer.Option(..., prompt=True)):
    typer.echo(f"Hello {name} {lastname}")"""

## OPTION WITH PROMPT CUZTOMIZED WITH CONFIRMATION
"""def main(name: str, lastname: str = typer.Option(..., prompt="Choisir un nom", confirmation_prompt=True)):
    typer.echo(f"Hello {name} {lastname}")"""

## OPTION WITH PROMPT CUZTOMIZED WITH CONFIRMATION HIDE INPUT 
"""def main(name: str, lastname: str = typer.Option(..., prompt="Choisir un nom", confirmation_prompt=True, hide_input=True)):
    typer.echo(f"Hello {name} {lastname}")"""

# OPTION WITH NAMED
"""def main(user_name: str = typer.Option(..., "--name", "-n")):
    typer.echo(f"Hello {user_name}")"""

# WITH CALLBACK
"""def name_callback(ctx: typer.Context, param: typer.CallbackParam, value: str):
    if ctx.resilient_parsing:
        return
    typer.echo(f"Validating YES param: {param.name}")
    if value != "Camila":
        raise typer.BadParameter("Only Camila is allowed")
    return value

def main(name: str = typer.Option(..., callback=name_callback)):
    typer.echo(f"Hello {name}")"""

# AUTO COMPLETION
"""def complete_name():
    return ["Camila", "Carlos", "Sebastian"]


def main(
    name: str = typer.Option(
        "World", help="The name to say hi to.", autocompletion=complete_name
    )
):
    typer.echo(f"Hello {name}")"""

# PROGRESS BAR 
"""def main():
    total = 0
    with typer.progressbar(range(1000), label="Processing") as progress:
        for value in progress:
            # Fake processing time
            time.sleep(0.1)
            total += 10
    typer.echo(f"Processed {total} things.")"""


def main():
    typer.echo("Opening Typer's docs")
    typer.launch("https://google.fr/")

if __name__ == "__main__":
    typer.run(main)
