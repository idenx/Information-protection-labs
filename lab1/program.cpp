#include "file_protector.hpp"
#include <iostream>

int main(int argc, char *argv[])
{
	Protection::FileProtector elf_protector;
	std::string msg = elf_protector.check_protection(argv[0]) ? "Congradulations! You`ve accesed file" :
		"You are not allowed to execute this file";
	std::cout << msg << std::endl;
}
