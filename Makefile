all:
	@cd 0-easy && make
	@cd 1-moderate && make
	@cd 2-hard && make

clean:
	@find . -type f -name "a.out" -exec rm -f {} \;
