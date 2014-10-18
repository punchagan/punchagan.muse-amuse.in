.PHONY: default clean related_test related_all

default: generate

generate: generate.cpp
	clang++ -g -Wall -Wextra -O2 -march=native -std=c++11 -o generate generate.cpp

related_all: generate
	./generate `find ../posts/ -iname "*.wp"` `find ../posts/ -iname "*.md"` `find ../posts/ -iname "*.rst"`

clean:
	rm -rf generate
