all:
	@cd 0-easy && $(MAKE)
	@cd 1-moderate && $(MAKE)
	@cd 2-hard && $(MAKE)

clean:
	@find . -type f -name "a.out" -exec rm -f {} \;
