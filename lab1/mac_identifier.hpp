#ifndef MAC_IDENTIFIER_HPP
#define MAC_IDENTIFIER_HPP

#include <string>
#include "computer_identifier.hpp"

namespace Protection {

	class MacIdentifier : public ComputerIdentifier {
	public:
		virtual const std::string get_identifier() const;
	};
}

#endif

