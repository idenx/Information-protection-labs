#include "file_protector.hpp"
#include "mac_identifier.hpp"
#include <fstream>

namespace Protection {
	FileProtector::FileProtector() : identifier(new MacIdentifier())
	{ }

	FileProtector::~FileProtector()
	{
		delete identifier;
	}

	bool FileProtector::protect(const std::string &file_name)
	{
		const std::string str_identifier = identifier->get_identifier();
		if (str_identifier.size() == 0 || str_identifier == "")
			return false;

		std::ofstream file(file_name.c_str(), std::ios_base::app);
		if (!file.good()) return false;
		file << str_identifier;
		return !file.fail();
	}

	bool FileProtector::check_protection(const std::string &file_name)
	{
		const std::string str_identifier = identifier->get_identifier();
		if (str_identifier.size() == 0 || str_identifier == "")
			return false;
		int id_size = str_identifier.size();

		std::ifstream file(file_name.c_str());
		file.seekg(-id_size, std::ios_base::end);
		if (!file.good()) return false;

		std::string identifier_in_file;
		file >> identifier_in_file;
		if (file.fail()) return false;

		return identifier_in_file == str_identifier;
	}
}

