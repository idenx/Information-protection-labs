#include "mac_identifier.hpp"
#include <fstream>

namespace Protection {
	const std::string MacIdentifier::get_identifier() const
	{
		if (cached_identifier != "")
			return cached_identifier;

		const char mac_address_path[] = "/sys/class/net/eth0/address";
		std::ifstream mac_file(mac_address_path, std::ios_base::in);

		std::string mac_address;
		mac_file >> mac_address;
		if (mac_file.fail()) return "";

		cached_identifier = mac_address;
		return mac_address;
	}
}

