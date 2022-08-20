#include "Ball.h"

Ball::Ball(RenderWindow* window)
{
	circle.setRadius(static_cast<float>(rand() % 21 + 5));
	Color enemyColor(rand() % 256, rand() % 256, rand() % 256);
	circle.setFillColor(enemyColor);
	circle.setPosition(
		Vector2f(static_cast<float>(rand() % window->getSize().x),
			static_cast<float>(rand() % window->getSize().y))
	);
}

Ball::~Ball()
{
}

//void Ball::update()
//{
//}

void Ball::draw(RenderTarget* target)
{
	target->draw(circle);
}

const CircleShape& Ball::getShape() const
{
	return circle;
}
