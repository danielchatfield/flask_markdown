try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name='flask_markdown',
	author='Daniel Chatfield',
	author_email='chatfielddaniel@gmail.com',
	version='0.0.1',
	ur='http://github.com/danielchatfield/flask_markdwon',
	py_modules=['flask_markdown'],
	description='A flask extension that adds a '
	            '{% markdown %} tag to templates.',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
	],
	install_requries=[
		'flask>=0.10.1',
		'jinja_markdown>=0.0.1'
	]
)