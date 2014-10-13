dirs=$(shell ls -1 | grep -v Makefile)

.PHONY: ${dirs}
all: ${dirs}

${dirs}:
	@cd $@ && if [ -f Makefile ]; then echo 'Building $@...' && $(MAKE); fi

clean:
	@find . -type f -name "a.out" -exec rm -f {} \;
