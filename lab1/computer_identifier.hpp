#ifndef COMPUTER_IDENTIFIER_HPP
#define COMPUTER_IDENTIFIER_HPP

#include <string>

namespace Protection {

	class ComputerIdentifier {
	protected:
		mutable std::string cached_identifier;
	public:
		ComputerIdentifier() : cached_identifier("") { }
		virtual const std::string get_identifier() const = 0;
	};
}

#endif

