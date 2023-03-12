import yaml
import subprocess
import sys


def main():
    args = sys.argv[1:]
    with open("./config.yaml", "r") as f:
        content = yaml.safe_load(f)

    cmd = args[0]
    inputDir = content['docker']['input-dir']
    outputDir = content['docker']['output-dir']
    imageName = content['docker']['name']
    platform = content['docker']['platform']

    if content['docker']['build']:
        buildWisecondor(imageName, platform)

    input = ['docker', 'run', '--rm',
             '--mount', 'type=bind,source=%s,target=/app/input' % inputDir,
             '--mount', 'type=bind,source=%s,target=/app/output' % outputDir,
             '%s:latest' % imageName] + args

    subprocess.run(input, stdout=sys.stdout, stderr=subprocess.STDOUT)


def buildWisecondor(imageName, platform):
    input = ['docker', 'build',
             '-t', imageName, '--platform=%s' % platform, '.']
    subprocess.run(input, stdout=sys.stdout,
                   stderr=subprocess.STDOUT, bufsize=1)


if __name__ == "__main__":
    main()
