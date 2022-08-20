#ifndef BALL_H_
#define BALL_H_

#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>

using namespace sf;

class Ball
{
public:
	// Constructor
	Ball(RenderWindow* window);
	virtual ~Ball();

	// Functions
	//void update();
	void draw(RenderTarget* target);
	const CircleShape& getShape() const; // return the circle shape

private:
	CircleShape circle;
};

#endif
