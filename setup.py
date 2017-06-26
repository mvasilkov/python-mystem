from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        name='python-mystem',

        version='0.0.3',

        description='Python wrapper for the MyStem morphological analyzer.',
        long_description='Python wrapper for the MyStem morphological analyzer.',

        url='https://github.com/mvasilkov/python-mystem',

        author='Mark Vasilkov',
        author_email='mvasilkov@gmail.com',

        license='MIT',

        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: Russian',
            'Programming Language :: Python :: 3',
            'Topic :: Text Processing :: Linguistic',
        ],

        keywords='natural-language-processing morphology MyStem Russian Yandex',

        packages=find_packages(),

        package_data={
            'mystem': ['bin/.gitignore'],
        },
    )
