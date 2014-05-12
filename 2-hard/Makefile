dirs=$(shell ls -1 | grep -v Makefile)

.PHONY: ${dirs}
all: ${dirs}

${dirs}:
	@cd $@ && if [ -f Makefile ]; then make; fi
