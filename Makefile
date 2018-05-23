# Makefile wrapper for waf

all:
	./waf

# free free to change this part to suit your requirements
configure:
	./waf configure --enable-examples --enable-tests --disable-gtk

build:
	./waf build

install:
	./waf install

clean:
	./waf clean

distclean:
	./waf distclean

from-scratch:
	./waf distclean
	./waf configure --enable-examples --enable-tests --disable-gtk --disable-python
	./waf build
