@echo off

if "%1" == "-h" ( echo build)
if "%1" == "" (
	py setup.py sdist bdist_wheel
	goto :EOF
)

if "%1" == "-h" ( echo install)
if "%1" == "install" (
	pip install --upgrade dist/pivot_point-0.1.0.tar.gz
	goto :EOF
)

if "%1" == "-h" ( echo test)
if "%1" == "test" (
	py -m unittest %2
	goto :EOF
)

