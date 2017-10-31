import os
from string import Template
from shutil import copyfile


template_str = Template('''#!/usr/bin/env python

import argparse
import sys
import os
import subprocess
from os.path import dirname
from pylint.lint import Run


ERROR_COUNT = $error_count
CONVENTION_COUNT = $convention_count
WARNINGS = $warnings
CODEBASE = '$codebase'
THRESHOLD_LINT_SCORE = $threshold_lint_score


def get_changed_files():
    """
    Get python files from 'files to commit' git cache list.
    """
    files = []
    out = subprocess.check_output(['git', 'diff', '--cached', '--name-status'])
    filelist = out.decode('ascii').strip()
    for line in filelist.split('\\n'):
        action, filename = line.strip().split()
        if filename.endswith('.py') and action != 'D':
            files.append(filename)
    return files


def run_pylint():
    changed_files = get_changed_files()
    results = Run(['--load-plugins=pylint_django', '--rcfile=pylintrc', *changed_files], exit=False)
    if results.linter.stats['error'] > ERROR_COUNT or \\
        results.linter.stats['convention'] > CONVENTION_COUNT or \\
        results.linter.stats['warning'] > WARNINGS or \\
        results.linter.stats['global_note'] < THRESHOLD_LINT_SCORE:
        print("Codebase has failed set standards, Please correct above mentioned issues before commit,"
              "Current Score is: %s, Errors: %s, Convention issues: %s, Warnings: %s" % (\\
            results.linter.stats['global_note'], results.linter.stats['error'], results.linter.stats['convention'],
            results.linter.stats['warning']))
        os._exit(1)

def main():
    SITE_ROOT = dirname(dirname(dirname(dirname(os.path.dirname(os.path.realpath(__file__))))))
    sys.path.append(SITE_ROOT)
    run_pylint()


if __name__ == "__main__":
    main()
''')

ERROR_COUNT = os.environ['ERROR_COUNT']
CONVENTION_COUNT = os.environ['CONVENTION_COUNT']
WARNINGS = os.environ['WARNINGS']
CODEBASE = os.environ['CODEBASE']
THRESHOLD_LINT_SCORE = os.environ['THRESHOLD_LINT_SCORE']

template_str = template_str.substitute(error_count=ERROR_COUNT, convention_count=CONVENTION_COUNT,
    warnings=WARNINGS, codebase=CODEBASE, threshold_lint_score=THRESHOLD_LINT_SCORE)

hook_file_path = os.path.join(CODEBASE, ".git/hooks/pre-commit")

with open(hook_file_path, "w") as text_file:
    text_file.write(template_str)

os.chmod(hook_file_path, 0o755)