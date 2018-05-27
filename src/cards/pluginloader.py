# -*- coding: utf-8 -*-
"""
pluginloader :  The API
  trained by dbader see https://www.youtube.com/watch?v=cbot48lckOs
usage: @TODO: use doctest here
>>> 
>>>
>>>
"""
import os
import sys
import importlib
import click

PLUGIN_NAME = 'plugins.card_column_projects' 
PLUGIN_FOLDER = os.path.join(os.path.abspath(os.curdir),'src', 'plugins')
COMMAND_FOLDER = os.path.join(os.path.abspath(os.curdir),'src', 'commands')


class CardsContext(object):
  def __init__(self):
    self.db = None 
    self.verbose = False
    self.home = os.getcwd()

  def log(self, message, *args):
    """log a message."""
    if args:
      message %= args
    click.echo(message,file=sys.stderr)

  def vlog(self, message, *args):
    """log a message, if verbose is enabled."""
    if self.verbose:
      self.log(message, *args)

pass_context = click.make_pass_decorator(CardsContext, ensure=True)

class PluginLoaderCLI(click.MultiCommand):
  
  def list_commands(self, ctx):
    result_commands = []
    extension = '.py'
    prefix = 'cmd_'
    start = len(prefix)
    end = len(extension)
    click.echo(COMMAND_FOLDER)
    for file_name in os.listdir(COMMAND_FOLDER):
      if file_name.endswith(extension) and \
        file_name.startswith(prefix):
        result_commands.append(file_name[start:-end])
    
    
    return result_commands

  def get_command(self, ctx, name):
    try:
      os.chdir('src')
      full_name = os.path.join(os.getcwd(),'src','commands',f'cmd_{name}')
      ##ctx.vlog(f'{name},full_name:{full_name}, exists: {os.path.exists(full_name+".py")}')
      mod = __import__('commands.cmd_' + name,
None, None, ['cli'])
      os.chdir('..')
    except ImportError as e:
      click.echo(f'could not import command: {name} from ({os.getcwd()}) ')
      # TODO: add error message here 
      return

    return mod.cli


#---- old code

def get_plugin_names(folder, extensions = ['.py']):
  plugin_names = []
  if os.path.exists(folder):
    files = os.listdir(folder)
    print (files)
    for file in files:
      base_name, file_extension = os.path.splitext(file)
      if file_extension in extensions:
        plugin_names.append(base_name)  
    
    return plugin_names

class PluginLoader(object):
  def __init__(self, path):
    self.path = path

  def __repr__(self):
    return f'PluginLoader {self.path}'

  def load(self):
    for plugin_name in get_plugin_names(PLUGIN_FOLDER):
      print(plugin_name)

    plugin_module = importlib.import_module(PLUGIN_NAME, '.')

    
