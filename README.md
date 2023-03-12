# WisecondorX
This is a wrapper script around a wisecondor docker. To use is youn first need to edit the config file:
`input-dir`: A local directory that is mounted onto `/app/input/` which contains any input resources you need to use.
`output-dir`: Same, but for output
`name`: the name of the docker image (used in build)
`build`: specified whether you need to build the image or not (set to false if you have already built it)
`platform`: The target platform(linux/amd64 or linux/x86_64 for example.)

## Getting Started
After the config setup you just run the python script and provide any argument that should be passed to WisecondorX after that:
```
python main.py ...args
```
