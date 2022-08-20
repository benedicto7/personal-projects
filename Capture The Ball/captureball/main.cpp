/*
Ben Elpidius
27 March 2022

Game:
	In this game, the player must capture the different balls that are spawned in the window
	by colliding with the balls. 

Bug:
	-Window collision lag
	-Spawning ball outside window

Improvements:
	-Make player bigger at every capture/collide with a ball.
	-Reset to normal size if it gets to a certain size or if player hits enemy objects. 
	-Add new entity/objects.
*/

#include <iostream>
#include <ctime>

#include "Game.h"
#include "Player.h"

using namespace std;

int main()
{
	// Time
	srand(static_cast<unsigned>(time(0)));

	// Launch game 
	Game game;

	// Game loop
	while (game.running())
	{
		game.update(); // creates the new image
		game.draw(); // draws the new image
	}

	return EXIT_SUCCESS;
}
