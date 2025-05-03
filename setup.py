from setuptools import setup, find_packages

setup(
    name='whatsapp_webhook',  # ✅ Must match inner folder and Git repo name
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
