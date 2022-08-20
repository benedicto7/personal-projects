#include "Game.h"

Game::Game()
{
	// Window
	window = new RenderWindow(VideoMode(1000.f, 800.f), "My First Game", Style::Close | Style::Titlebar);
	initVariable(); // ???
	window->setFramerateLimit(60);

	// Ball
	maxBalls = 25;
	spawnTimerMax = 15.f;
	spawnTimer = spawnTimerMax;

	// Points
	points = 0;	

	// Font and Text
	font.loadFromFile("Fonts/pixel-millennium.regular.ttf");
	text.setFont(font);
	text.setFillColor(Color::White);
	text.setCharacterSize(24);
	text.setStyle(Text::Bold);
}

Game::~Game()
{
	delete window;
}

void Game::initVariable()
{
	endGame = false;
}

const bool Game::running() const
{
	return window->isOpen();
}

void Game::update()
{
	pollEvents();
	spawnBall();
	player.update();
	updateCollision();
	updateGUI();
}

void Game::draw()
{
	window->clear();

	// Player
	player.draw(window);

	// Ball		
	for (auto &i : ball) // ???
	{
		i.draw(window);
	}

	// Gui-text and font
	renderGUI(window);

	window->display();
}

void Game::pollEvents()
{
	while (window->pollEvent(event))
	{
		switch (event.type)
		{
		case Event::Closed:
			window->close();
			break;

		case Event::KeyPressed:
			switch (event.key.code)
			{
			case Keyboard::Escape:
				window->close();
				break;
			}

		}
	}

}

// Spawn timer
void Game::spawnBall()
{
	if (spawnTimer < spawnTimerMax)
	{
		spawnTimer += 0.5f;
	}

	else
	{
		if (ball.size() < maxBalls)
		{
			ball.push_back(Ball(window)); // ???
			spawnTimer = 0.f;
		}
	}
}

void Game::updateCollision()
{
	// Check collision
	for (size_t i = 0; i < ball.size(); i++)
	{
		if (player.getShape().getGlobalBounds().intersects(ball[i].getShape().getGlobalBounds()))
		{
			ball.erase(ball.begin() + i);
			points += 1;
		}
	}
}

void Game::renderGUI(RenderTarget* target)
{
	window->draw(text);
}

void Game::updateGUI()
{
	// Cout the points to window
	stringstream ss;
	ss << "Points: " << points;

	text.setString(ss.str());
}
