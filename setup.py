from setuptools import setup, find_packages

setup(
    name='whatsapp_webhook',
    version='0.0.1',
    description='Webhook for WhatsApp Meta API',
    author='Yusuf Paloba',
    author_email='yusufpaloba43@outlook.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
