#include "Player.h"

// Constructors
Player::Player()
{
	// Sprite
	texture.loadFromFile("piskel.png");
	texture.setSmooth(true);
	player.setTexture(texture);
	player.setScale(Vector2f(0.5f, 0.5f));
	player.setPosition(500 - (player.getGlobalBounds().width / 2), 400 - (player.getGlobalBounds().height / 2));

	movementSpeed = 8.f;
}

Player::~Player()
{
}

void Player::windowCollision()
{
	// Left collision
	if (player.getGlobalBounds().left <= 0.f)
	{
		player.setPosition(0.f, getY());
	}
	// Top collision
	if (player.getGlobalBounds().top <= 0.f)
	{
		player.setPosition(getX(), 0.f);
	}
	// Right collision
	if (player.getGlobalBounds().left + player.getGlobalBounds().width >= 1000.f)
	{
		player.setPosition(1000 - player.getGlobalBounds().width, getY());
	}
	// Bottom collision
	if (player.getGlobalBounds().top + player.getGlobalBounds().height >= 800.f)
	{
		player.setPosition(getX(), 800 - player.getGlobalBounds().height);
	}
}

// Player movement
void Player::playerMovement()
{
	if (Keyboard::isKeyPressed(Keyboard::A))
	{
		player.move(-movementSpeed, 0.f);
	}

	if (Keyboard::isKeyPressed(Keyboard::D))
	{
		player.move(movementSpeed, 0.f);
	}

	if (Keyboard::isKeyPressed(Keyboard::W))
	{
		player.move(0.f, -movementSpeed);
	}

	if (Keyboard::isKeyPressed(Keyboard::S))
	{
		player.move(0.f, movementSpeed);
	}
}

void Player::update()
{
	// Window collision
	windowCollision();

	// Player movement
	playerMovement();
}

const Sprite& Player::getShape() const
{
	return player;
}

void Player::draw(RenderTarget* target)
{
	target->draw(player);
}

float Player::getX()
{
	return player.getPosition().x;
}

float Player::getY()
{
	return player.getPosition().y;
}

