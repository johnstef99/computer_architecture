
SOURCES= spec.c blocksort.c bzip2.c bzlib.c compress.c crctable.c \
	 decompress.c huffman.c randtable.c

DC=../../../../../../../dockcross-linux-armv7
CFLAGS=-O0
COMP_FLAGS=-lm -DSPEC_CPU -DNDEBUG -static

all: $(SOURCES)
	#sudo $(CC) $(COMP_FLAGS) $(SOURCES) $(CFLAGS) -o specbzip
	sudo $(DC) -c '$$CC $(COMP_FLAGS) $(SOURCES) $(CFLAGS) -o specbzip'
