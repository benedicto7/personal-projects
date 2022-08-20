#ifndef PLAYER_H_
#define PLAYER_H_

#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>

using namespace sf;

class Player
{
public:
	// constructor
	Player();
	virtual ~Player();

	// functions
	void update();
	void playerMovement();
	void windowCollision();
	//const bool checkCollision();
	const Sprite& getShape() const; // returns the player sprite
	void draw(RenderTarget* target);
	float getX();
	float getY();

private:
	// Create player
	Texture texture;
	Sprite player;

	float movementSpeed;
};

#endif 
