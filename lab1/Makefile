all: clean program installer
	rm -f *.o

program: protector program.cpp
	g++ -g -o program program.cpp file_protector.o mac_identifier.o
installer: protector installer.cpp
	g++ -g -o installer installer.cpp file_protector.o mac_identifier.o

protector: file_protector.cpp mac_identifier.cpp
	g++ -c -g file_protector.cpp mac_identifier.cpp

clean:
	rm -f program installer *.o
