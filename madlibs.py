# https://www.nytimes.com/2021/05/08/business/bill-melinda-gates-divorce-foundation.html
from rich.console import Console
from rich.table import Table


name1 = input("What is the name of your Dog: ")
name2 = input("What is the name of your Cat: ")
place = input("Last place you fucked: ")
swear = input("Name a swear work: ")
food = input("Your favourite meal: ")
professor = input("Full name of your professor: ")
aliens = input("Name a race of aliens(plural): ")

title = f"The Separate Worlds of {name1} and {name2}"

text = f"[bold sea_green2]{name1}[/] and [bold sea_green2]{name2}[/] were stuck at \
[bold sea_green2]{place}[/].\n\nWhen the [bold sea_green2]{swear}[/] hit last March, the couple retreated to their \
66,000-square-foot [bold sea_green2]{place}[/] on the shore of Lake Washington, venturing \
out infrequently to minimize their potential exposure to the [bold sea_green2]{swear}[/]. \
From their [bold sea_green2]{place}[/] offices they continued running the influential \
foundation that bears their name, video chatting with world \
[bold sea_green2]{aliens}[/] to secure financial commitments for [bold sea_green2]{food}[/] distribution, \
and talking about the health of American democracy with their \
youngest [bold sea_green2]{professor}[/], who was finishing her senior year of high school \
remotely.\n\nFor a couple who had spent much of the past three decades \
traveling the world, so much time together at [bold sea_green2]{place}[/] was an abrupt \
change of pace. “Working from [bold sea_green2]{place}[/] — that was a piece that I think \
we hadn’t really individually prepared for quite as much,” \
[bold sea_green2]{name2}[/] told The New York Times in October.\n:heart::heart::heart:"

table = Table(title="Read All About It - New York Times!")
table.add_column(title)
table.add_row(text)


console = Console()
console.print(table)
