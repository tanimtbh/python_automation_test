import os
import time
#import your library library
try:
    import git
except:
    stream = os.popen('pip install GitPython')
    time.sleep(80)
finally:
    import git




def main():
    print("Hi selfInject() git")
    repo = git.Repo(os.getcwd())
    current = repo.head.commit
    repo.remotes.origin.pull()
    if current != repo.head.commit:
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")
                print("Git changed")

    try:
        if os.name in ('nt', 'dos'):
            if os.popen('python --version').read():
                print("python found")
                os.system('python main.py')
                print("main.py started")
            else:
                 raise Exception('python main.py can not run on windows')
               
        else:
            raise Exception('python main.py can not run on windows')
    except Exception as error:
        os.system('python3 main.py')
        print("main.py started")
    finally:
        print("App.py completed its task and handover to main.py")

if __name__ == "__main__":
    main()