import click
from cards import pass_context
import json

@click.command('export', short_help='Export todos.')
@click.option('-n', '--noowner', default=None, is_flag=True,
              help='filter on the card without owners')
@click.option('-o', '--owner', default=None,
              help='filter on the card owner')
@click.option('-d', '--done', default=None,
              type=bool,
              help='filter on cards with given done state')
@pass_context
def cli(ctx, noowner, owner, done):

    """Shows file changes in the current working directory."""

    ctx.vlog('export as ...')

    cards = ctx.db.list_cards(noowner, owner, done)
    export = []
    for card in cards:
        export.append( card.to_dict())
    click.echo(export)
    