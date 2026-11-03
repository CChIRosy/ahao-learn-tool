"""Run the packaged CLI from an isolated extraction with synthetic learner data."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--package', required=True, type=Path)
    package = parser.parse_args().package.resolve()
    with tempfile.TemporaryDirectory(prefix='campus-gap-smoke-') as directory:
        directory = Path(directory)
        root, data = directory / 'skill', directory / 'data'
        root.mkdir()
        with zipfile.ZipFile(package) as archive:
            assert archive.testzip() is None
            archive.extractall(root)
        command = [sys.executable, '-X', 'utf8', str(root / 'scripts/diagnose.py')]

        def run(arguments):
            result = subprocess.run(command + arguments, cwd=directory,
                                    capture_output=True, text=True, encoding='utf-8', check=True)
            return json.loads(result.stdout)

        courses = run(['courses'])
        assert len(courses) == 15
        assert any(row['id'] == 'math02.chain' for row in run(['search', '--query', '链式法则']))
        profile = ['--profile', 'smoke', '--data-dir', str(data)]
        assert run(profile + ['start', '--skill', 'math02.chain'])['id'] == 'math02.chain.1'
        assert run(profile + ['answer', '--answer', 'cos(x**2)'])['verdict'] == 'incorrect'
        assert run(profile + ['next'])['id'] == 'math02.basic.1'
        run(profile + ['hint'])
        run(profile + ['answer', '--answer', 'cos(u)'])
        assert any(row['status'] == '提示后完成' for row in run(profile + ['report'])['nodes'])
        output = directory / 'card.md'
        subprocess.run([sys.executable, '-X', 'utf8', str(root / 'scripts/report.py'),
                        '--profile', 'smoke', '--data-dir', str(data), '--output', str(output)],
                       cwd=directory, check=True, capture_output=True)
        assert '卡点证据卡' in output.read_text(encoding='utf-8')
        print(json.dumps({'package': package.name, 'zip_extraction_smoke': 'passed',
                          'modules': len(courses), 'report_generated': True}, ensure_ascii=False))


if __name__ == '__main__':
    main()
