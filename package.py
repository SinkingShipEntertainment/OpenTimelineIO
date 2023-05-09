name = 'otio'

version = '0.15.0.sse.1.0.0'

authors = [
    'Pixar',
]

description = '''Open Timeline IO'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['SSE_REZ_REPO_RELEASE_EXT']

requires = [
    "rapidjson-1.1.0",
    "pybind11-2.6.2",
    "imath-3.1.5",
]

private_build_requires = [
]

variants = [
    ['platform-linux', 'arch-x86_64', 'os-centos-7', "python-3.9.7"],
]

def pre_build_commands():
    command("source /opt/rh/devtoolset-9/enable")

def commands():
    env.REZ_OTIO_ROOT = '{root}'
    env.PYTHONPATH.append('{root}/python')

uuid = 'repository.OpenTimelineIO'
build_system = "cmake"
