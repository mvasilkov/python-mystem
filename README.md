    git clean -dfx
    python setup.py bdist_wheel
    twine upload dist/*.whl
