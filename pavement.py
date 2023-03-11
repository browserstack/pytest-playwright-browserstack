from paver.easy import *
from paver.setuputils import setup
#from multiprocess import Process
import threading, os
import platform
import json
from browserstack.local import Local
from multiprocessing import Lock

bs_local = None
local_flag = False
lock=Lock()


setup(
    name = "pytest-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("PyTest Playwright Integration with BrowserStack"),
    license = "MIT",
    keywords = "example Playwright browserstack",
    url = "https://github.com/browserstack/pytest-browserstack",
    packages=['tests']
)

def run_py_test(config, run_type, task_id=0):
    print("Thread "+threading.current_thread().name+"; Thread count =>"+str(threading.active_count()))
    if config == 'local' and run_type == 'remote':
        if platform.system() == "Windows":
            sh('cmd /C "set CONFIG_FILE=resources/%s.json && set TASK_ID=%s && set REMOTE=true && pytest -s src/tests/sample-local-test.py --base-url http://bs-local.com:45454"' % (config, task_id))
        else:
            sh('CONFIG_FILE=resources/%s.json TASK_ID=%s REMOTE=true pytest -v -s src/tests/sample-local-test.py --base-url http://bs-local.com:45454' % (config, task_id))
    elif run_type == 'remote':
        if platform.system() == "Windows":
            sh('cmd /C "set CONFIG_FILE=resources/%s.json && set TASK_ID=%s && set REMOTE=true && pytest -s src/tests/sample-test.py --base-url https://bstackdemo.com"' % (config, task_id))
        else:
            sh('CONFIG_FILE=resources/%s.json TASK_ID=%s REMOTE=true pytest -s src/tests/sample-test.py --base-url https://bstackdemo.com' % (config, task_id))
    else:
        if platform.system() == "Windows":
            sh('cmd /C "set CONFIG_FILE=resources/%s.json && set TASK_ID=%s && set REMOTE=false && pytest -s src/tests/sample-test.py --base-url https://bstackdemo.com"' % (config, task_id))
        else:
            sh('CONFIG_FILE=resources/%s.json TASK_ID=%s REMOTE=false pytest -s src/tests/sample-test.py --base-url https://bstackdemo.com' % (config, task_id))
    if local_flag:
        lock.acquire()
        try:
            print("Thread count after yield: " + str(threading.active_count()))
            if threading.active_count() <= 2:
                # Stop Local
                stop_local()
        finally:
                lock.release()
                print("Finally")

@task
@consume_nargs(2)
def run(args):
    """Run single, local and parallel test using different config."""
    jobs = []
    print(*args)
    config_file = 'resources/%s.json' % (args[0])
    with open(config_file) as data_file:
        CONFIG = json.load(data_file)
    environments = CONFIG['environments']
    global local_flag
    if "local" in CONFIG["capabilities"] and CONFIG["capabilities"]["local"]:
        access_key = os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else \
        CONFIG["key"]
        print("local is set to true")
        local_flag=True
        start_local(access_key)
    else:
        print("local is set to false")
        local_flag=False
    for i in range(len(environments)):
        #p = Process(target=run_py_test, args=(args[0], args[1], i))
        p = threading.Thread(target=run_py_test, args=(args[0], args[1], i), name=str(i))
        jobs.append(p)
        p.start()
        


def start_local(access_key):
    print("Starting Local")
    """Code to start browserstack local before start of test."""
    global bs_local
    bs_local = Local()
    bs_local_args = {"key": access_key}
    bs_local.start(**bs_local_args)


def stop_local():
    print("Stopping Local")
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()