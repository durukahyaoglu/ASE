'''These modules used to check system and run application'''
import platform
from fabric.api import local, shell_env

def prepare_deploy():
    '''Run all tests, initialize server and db, and run app'''
    static_analyzer()
    run_tests()
    init_server()
    run_server()

def quick_deploy():
    '''No tests or static analysis, only use for repeated debugging'''
    init_server()
    run_server()

def static_analyzer():
    '''Runs Pylint analyzer'''
    local("pylint app.py")

def run_tests():
    '''Perform tests here'''

def init_server():
    '''Initializes the server'''
    if platform.system() == 'Windows':
        # SET DOES NOT SEEM TO BE WORKING FROM HERE
        local("set FLASK_APP=app.py")
        local('flask initdb')
    else:
        with shell_env(FLASK_APP='app.py'):
            local('flask initdb')

def run_server():
    '''Runs the application'''
    if platform.system() == 'Windows':
        local('flask run')
    else:
        with shell_env(FLASK_APP='app.py'):
            local('flask run')
