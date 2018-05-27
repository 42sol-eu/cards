import click
from cards import pass_context


@click.command('disable', short_help='Disable plugins.')
@click.option('-a', '--all', is_flag=True, help='Disable all plugins.')
@pass_context
def cli(ctx, all):
    """Shows file changes in the current working directory."""

    # TODO: implement functions to plugin disable

    if all:
      ctx.log('disable plugins: all')
    else:
      ctx.log('disable plugins: ?')
      
    ##ctx.vlog('bla bla bla, debug info')