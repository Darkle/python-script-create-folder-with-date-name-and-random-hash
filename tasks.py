import os

from invoke import task
from watchgod import run_process

@task
def cocowatch(context):
    print("cocowatch running")
    os.system("coconut ./ --watch --package --strict --target sys")

def runProspector():
    # os.system('prospector app.py --with-tool pyroma --with-tool vulture')
    """
    Vulture doesn't seem to be working properly. Get an error of:
        Line: None
        vulture: failure / Tool vulture failed to run (exception was raised)
    https://github.com/landscapeio/prospector/issues?utf8=%E2%9C%93&q=vulture
    """
    os.system('prospector app.py --with-tool pyroma')

@task
def lintwatch(context):
    print("lintwatch running")
    run_process('./', runProspector)

def runApp():
    os.system('python app.py')

@task
def appwatch(context):
    print("appwatch running")
    run_process('./', runApp)

def runMypy():
    os.system('mypy app.py --follow-imports=silent')

@task
def mypyWatch(context):
    print("mypyWatch running")
    run_process('./', runMypy)
