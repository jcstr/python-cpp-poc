#include <iostream>
#include <fstream>

int main() {
	std::ofstream file("test.txt");
	
	file << "Hello from file!\n" << std::endl;
	
	std::ifstream f("test.txt");
	if (file.is_open()) {
		std::cout << f.rdbuf();
	}

	return 0;
}
