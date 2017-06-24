from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        name='python-mystem',

        version='0.0.2',

        description='Python MyStem',
        long_description='Python MyStem',

        url='https://github.com/mvasilkov/python-mystem',

        author='Mark Vasilkov',
        author_email='mvasilkov@gmail.com',

        license='MIT',

        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
        ],

        keywords='mystem',

        packages=find_packages(),

        package_data={
            'mystem': ['bin/.gitignore'],
        },
    )
