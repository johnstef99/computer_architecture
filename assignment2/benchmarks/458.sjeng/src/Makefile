
SOURCES= attacks.c book.c crazy.c draw.c ecache.c epd.c eval.c leval.c \
	 moves.c neval.c partner.c proof.c rcfile.c search.c see.c seval.c \
	 sjeng.c ttable.c utils.c

CC=arm-linux-gnueabihf-gcc
CFLAGS=-O0
COMP_FLAGS=-lm -DSPEC_CPU -DNDEBUG -static

all: $(SOURCES)
	$(CC) $(COMP_FLAGS) $(SOURCES) $(CFLAGS) -o specsjeng



