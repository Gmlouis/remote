import pkg_resources

def min_python_version():
    dependencies = pkg_resources.working_set
    versions = (tuple(map(int, req.specifier.version)) for dep in dependencies for req in dep.requires() if req.project_name == 'python')
    return max(versions, default=(0, 0))

print(f"Minimum Python version required: {min_python_version()}")
