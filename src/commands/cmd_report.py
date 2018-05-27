import click
from cards import pass_context


@click.command('report', short_help='Shows file changes.')
@pass_context
def cli(ctx):
    """Shows file changes in the current working directory."""
    ctx.log('Changed plugins: none')
    ##ctx.vlog('bla bla bla, debug info')