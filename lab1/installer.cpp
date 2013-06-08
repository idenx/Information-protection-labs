#include <iostream>
#include "file_protector.hpp"

int main(int argc, char *argv[])
{
	if (argc != 2) {
		std::cerr << "Usage: `" << argv[0] << " program_filename'" << std::endl;
		return 1;
	}

	const char *program_filename = argv[1];
	Protection::FileProtector elf_protector;
	if (!elf_protector.protect(program_filename)) {
		std::cerr << "Can't protect file `" << program_filename << "'" << std::endl;
		return 1;
	}

	std::cout << "Successfully protected" << std::endl;
	return 0;
}

