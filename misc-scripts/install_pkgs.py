import subprocess

def install_package(package):
    try:
        subprocess.check_call([f"pip install {package}"], shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    with open('requirements.txt', 'r') as req_file:
        packages = req_file.readlines()

    failed_packages = []

    for package in packages:
        package = package.strip()
        if not install_package(package):
            failed_packages.append(package)

    if failed_packages:
        with open('failed_requirements.txt', 'w') as fail_file:
            for package in failed_packages:
                fail_file.write(f"{package}\n")

if __name__ == "__main__":
    main()
