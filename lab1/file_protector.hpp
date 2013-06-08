#ifndef FILE_PROTECTOR_HPP
#define FILE_PROTECTOR_HPP

#include "computer_identifier.hpp"
#include <string>

namespace Protection {

	class FileProtector {
	private:
		const ComputerIdentifier *identifier;
	public:
		FileProtector();
		~FileProtector();
		bool protect(const std::string &file_name);
		bool check_protection(const std::string &file_name);
	};
}

#endif

