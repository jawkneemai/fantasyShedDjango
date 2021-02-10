#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dataShed.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__': 
    main()
# We can use this convention block to allow or prevent parts of code from being run when the modules are imported (as opposed to the file being run itself)
# i.e. 
# else: 
    # run_another_function() // This function will run when manage.py is being imported as a module because the other script importing will have possession of '__main__'
