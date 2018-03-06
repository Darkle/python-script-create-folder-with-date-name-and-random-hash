import os

from invoke import task
from watchgod import run_process

@task
def cocowatch(context):
    print("cocowatch running")
    os.system("coconut ./ --watch --standalone --strict --target sys")

def runProspector():
    os.system('prospector app.py')

@task
def lintwatch(context):
    print("lintwatch running")
    run_process('./', runProspector)

def runProgram():
    os.system('python app.py')

@task
def programwatch(context):
    print("programwatch running")
    run_process('./', runProgram)
