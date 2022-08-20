#ifndef GAME_H_
#define GAME_H_

#include <sstream>

#include "Player.h"
#include "Ball.h"

using namespace std;

class Game
{
public:
	// Constructors
	Game();
	virtual ~Game();

	// Functions
	void update();
	void draw();
	const bool running() const;
	void pollEvents();
	void spawnBall();
	void updateCollision(); // collision with an object
	void renderGUI(RenderTarget* target);
	void updateGUI();

private:
	// Display window
	RenderWindow* window;

	// Handles event
	Event event;
	bool endGame;

	// Functions	
	void initVariable();

	// Player
	Player player;

	// Ball
	vector<Ball> ball;

	// Timer
	unsigned maxBalls;
	float spawnTimer;
	float spawnTimerMax;

	// Enemy
	//vector<Enemy> enemy;

	// Points
	Font font;
	Text text;
	int points;
};

#endif
