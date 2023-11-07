# Makefile for Sacalon
clean:
	rm -rf dist build
clean-windows:
	del dist
	del build
deps :
	python3 --version
	pip3 --version
	pip3 install -r requirements.txt
deps-windows:
	python --version
	pip --version
	pip install -r requirements.txt
build: deps
	pyinstaller --add-data src/hlib:hlib "src/sacalon.py" --name "sacalon" --noconfirm --onefile --console
	cp -r src/hlib dist/
	cp -r examples/ dist/
windows: deps-windows clean-windows
	pyinstaller --add-data src\hlib;hlib "src\sacalon.py" --name "sacalon" --noconfirm --onefile --console
	xcopy src\hlib dist\hlib /E /H /C /I
	xcopy examples dist\examples /E /H /C /I
path:
	cp dist/sacalon usr/local/bin/sacalon
tests:
	cd tests && $(MAKE) tests && cd ..

.PHONY: all clean deps deps-windows build windows path tests