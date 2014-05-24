SUBDIRS = hello

bin_SCRIPTS = hello-world
CLEANFILES = $(bin_SCRIPTS)
EXTRA_DIST = hello-world.in

do_substitution = sed -e 's,[@]pythondir[@],$(pythondir),g' \
		      -e 's,[@]PACKAGE[@],$(PACKAGE),g' \
		      -e 's,[@]VERSION[@],$(VERSION),g'

hello-world: hello-world.in Makefile
	$(do_substitution) < $(srcdir)/hello-world.in > hello-world
	chmod +x hello-world

