//
//  main.cpp
//  Game_Engine
//
//  Created by Skyy Siejko on 4/4/18.
//  Copyright © 2018 Skyy Siejko. All rights reserved.
//
#define _USE_MATH_DEFINES
#include <SDL2/SDL.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <cmath>
#include <stdio.h>
#define NO_SDL_GLEXT


bool InitEverything();
bool InitSDL();
bool CreateWindow();
bool CreateRenderer();
void SetupRenderer();

void Render();
void RunGame();
bool loop = true;

// Window pos
int posX = 900;
int posY = 300;
int sizeX = 300;
int sizeY = 400;

SDL_Window* window;
SDL_Renderer* renderer;



int randomNum(int num)
{
    return floor(rand()*num)+1;

}



struct Point
{
    float x, y;
    bool intersects;

    Point(float x_, float y_)
    {
        x = x_;
        y = y_;
    }
};



template <typename T>
class Math
{
public:
    float epsilon = 0.00001;

    float distance(T a, T b)
    {
        return sqrt((a*a)+(b*b));
    }


    float n_x(float x1, float y1, float x2, float y2)
    {
        return -(y2-y1)/ distance(x2-x1, y2-y1);
    }

    float n_y(float x1, float y1, float x2, float y2)
    {
        return -(x2-x1)/ distance(x2-x1, y2-y1);
    }

    bool point_In_Rect(float X, float Y, T r)
    {
        bool inside = true;

        float nx = n_x(r.x,r.y,r.x+r.width,r.y);
        float ny = n_y(r.x,r.y,r.x+r.width,r.y);
        float distance = ((r.x-X)*nx+ (r.y-Y)* ny);
        if (distance > epsilon){
            inside = false;
        }

        nx = n_x(r.x+r.width, r.y, r.x+r.width, r.y+r.height);
        ny = n_y(r.x+r.width, r.y, r.x+r.width, r.y+r.height);
        distance = ((r.x+r.width - X) * nx + (r.y - Y) * ny);
        if(distance > epsilon){
            inside = false;
        }

        nx = n_x(r.x+r.width, r.y+r.height, r.x, r.y+r.height);
        ny = n_y(r.x+r.width, r.y+r.height, r.x, r.y+r.height);
        distance = ((r.x+r.width - X) * nx + (r.y+r.height - Y) * ny);
        if(distance > epsilon){
            inside = false;
        }

        nx = n_x(r.x, r.y+r.height, r.x, r.y);
        ny = n_y(r.x, r.y+r.height, r.x, r.y);
        distance = ((r.x - X) * nx + (r.y+r.height - Y) * ny);
        if(distance > epsilon){
            inside = false;
        }
        return inside;

    }

    Point getIntersection(float x1, float y1, float x2, float y2, float x3, float y3, float x4, float y4)
    {
        float denom = ((x2-x1)*(y4-y3)-(y2-y1)*(x4-x3));
        float r,s,x,y;
        bool b;
        if(denom != 0){
            //Intersection in ray "local" coordinates
            r = (((y1 - y3) * (x4 - x3)) - (x1 - x3) * (y4 - y3)) / denom;
            //Intersection in segment "local" coordinates
            s = (((y1 - y3) * (x2 - x1)) - (x1 - x3) * (y2 - y1)) / denom;
            //The algorithm gives the intersection of two infinite lines, determine if it lies on the side that the ray is defined on
            if (r >= 0)
            {
                //If point along the line segment
                if (s >= 0 && s <= 1)
                {
                    b = true;
                    //Get point coordinates (offset by r local units from start of ray)
                    x = x1 + r * (x2 - x1);
                    y = y1 + r * (y2 - y1);
                }
            }
        }
        Point p(x,y);
        p.intersects = b;
        return p;
    }


};

template <typename T>
Math <T> math;

class Seed{
public:
    float x,y,radius;

    Seed(float x_, float y_, float radius_ )
    {
        x = x_;
        y = y_;
        radius = radius_;
    }


};





struct Barrier
{
    float x, y;
    float point_count;
    std::vector<Point> points;

    Barrier(float x_, float y_, float  point_count_, std::vector<Point> points_)
    {
        x = x_;
        y = y_;
        point_count = point_count_;
        points = points_;
    }
};

class Objects
{
public:
    int barrier_size = 15;
    float x,y,z;
    float point_count = floor(rand()*randomNum(7)+3);
    float step = 2*M_PI/point_count;
    float offSet;
    std::vector <Seed> seeds;
    float delta = fmin(sizeX,sizeY)/(barrier_size/2);
    std::vector<Point> points;
    std::vector<Barrier> barriers;





    void createSeeds()
    {
        while (seeds.size() < barrier_size)
        {
            Seed seed(randomNum(sizeX-delta-delta)+delta,randomNum(sizeY-delta-delta)+delta,delta);
            if(! math<float>.point_In_Rect(seed.x, seed.y, seed.radius))
            {
                seeds.push_back(seed);
            }
        }

        for (int i =0; i <seeds.size()-1; i++)
        {
            for(int j = i+1; j < seeds.size(); j++)
            {
                float distance = math<float>.distance(seeds[i].x-seeds[j].x, seeds[i].y-seeds[j].y);
                if ((distance/2) < seeds[i].radius){
                    seeds[i].radius = distance/2;
                }if ((distance/2) < seeds[j].radius){
                    seeds[j].radius = distance/2;
                }
            }
        }

    }

    void createPolygons()
        {
            float ax =0;
            float by = 0;
        for (int i = 0; i < seeds.size(); i ++){
            ax = seeds[i].x;
            by = seeds[i].y;
        }
        for (int p = 0; p < point_count; p++){
            Point point(ax-seeds[p].radius*cos(step*p+offSet), by+seeds[p].radius*sin(step*p+offSet));
        }

        Barrier barrier(ax, by, point_count, points);

    }




};


struct Corner
{

};


class Vector3D
{
    public:
        float x,y,z, magnitude, frequency;
        int direction;
        std::vector <float> values{3};


    Vector3D(float x_, float y_, float z_, int dir_)
    {
        x = x_;
        y = y_;
        z = z_;
        direction = dir_;
    }


    float dotProductAngle(Vector3D vector, float theta)
    {
        return magnitude*vector.magnitude* cos(theta);
    }

    float dotProduct(Vector3D vector)
    {
        return (x*vector.x)+ (y*vector.y)+ (z*vector.z);
    }

    std::vector <float> twoDRotate(float theta, int i, int j)
    {
        float iRot = values[i]*cos(theta) - values[j]*sin(theta);
        float jRot = values[i]*sin(theta) + values[j]*cos(theta);
        return {iRot, jRot};
    }

    std::vector <float> threeD_Rotate_X(float theta, int i, int j, int k)
    {
        float jRot = values[i]*cos(theta) - values[j]*sin(theta);
        float kRot = values[i]*sin(theta) + values[j]*cos(theta);
        return { (float) i, jRot, kRot};

    }

    std::vector <float> threeD_Rotate_Y(float theta, int i, int j, int k)
    {
        float iRot = values[i]*cos(theta) - values[j]*sin(theta);
        float kRot = values[i]*sin(theta) + values[j]*cos(theta);
        return { iRot,  (float) j, kRot};

    }


    std::vector <float> threeD_Rotate_Z(float theta, int i, int j, int k)
    {
        float iRot = values[i]*cos(theta) - values[j]*sin(theta);
        float jRot = values[i]*sin(theta) + values[j]*cos(theta);
        return { iRot,  jRot, (float) k};

    }

    bool isOrthogonal(Vector3D vector){
        return dotProduct(vector) == 0;
    }

};

class Light: public Objects
{
public:
    std::vector<Point> corners;
    std::vector <Objects> objects;
    std::vector <Point> vertices;
    std::vector <std::vector <Point>> maxLimits;
    std::vector <std::vector <Point>> minLimits;
    std::vector <Objects> lights;
    std::vector <float> angles;




    void maxBoundry()
    {
        Point minPoint(0,0);
        for(int i = 0; i < lights.size(); i ++)
        {
            maxLimits.push_back({Point(corners[0].x, corners[0].y),Point(corners[1].x, corners[1].y), Point(corners[2].x, corners[2].y), Point(corners[3].x, corners[3].y)});
            for(int r = 4; r < vertices.size(); r++){
                Point p1 = math.getIntersection(lights[i].x, lights[i].y, vertices[r].x, vertices[r].y, 0, 0, (float)sizeX, 0);
                Point p2 = math.getIntersection(lights[i].x, lights[i].y, vertices[r].x, vertices[r].y, (float) sizeX, 0, (float)sizeX, (float) sizeY);
                if (p1.intersects && p2.intersects)
                    maxLimits.push_back({p1,p2});
                Point p3 = math.getIntersection(lights[i].x, lights[i].y, vertices[r].x, vertices[r].y, (float) sizeX, (float) sizeY, 0, (float) sizeY);
                Point p4 = math.getIntersection(lights[i].x, lights[i].y, vertices[r].x, vertices[r].y, 0, (float) sizeY, 0, 0);
                if(p2.intersects && p3.intersects)
                    maxLimits.push_back({p3,p4});
        }

            for (int s = 0; s < vertices.size(); s++){
                minPoint.x = maxLimits[s][0].x;
                minPoint.y = maxLimits[s][1].y;
                for(int t = 0; t < barriers.size(); t++){
                    for(int u = 0; u < barriers[t].point_count; u++){
                        Point p = math.getIntersection(lights[i].x, lights[i].y, vertices[s].x, vertices[s].y, barriers[t].points[u].x, barriers[t].points[u].y,(float) barriers[t].points[(t+1)/barriers[t].point_count].x,(float) barriers[t].points[(t+1)/(barriers[t].point_count)].y);

                        if (p.intersects){
                            if ((math.distance(lights[i].x- p.x, lights[i].y -p.y)) < math.distance(lights[i].x - minPoint.x, lights[i].y-minPoint.y)){
                                minPoint.x = p.x;
                                minPoint.y = p.y;
                            }
                        }

                    }
                }
                minLimits.push_back({Point(minPoint.x, minPoint.y)});
            }

    }
    }

    void sort_angles(Point a, Point b){
        for(int i = 0; i < lights.size(); i++){
            angles.push_back(atan2(a.x-lights[i].x, a.y-lights[i].y)- atan2(b.x-lights[i].x, b.y -lights[i].y));
        }

        //still need to sort here

    }



    void draw(){

        for (int i = 0; i < lights.size(); i++)
        {
            if (lights[i].x < 20) {
                lights[i].x = 20;
            }
            if (lights[i].y < 20) {
                lights[i].y = 20;
            }
            if (lights[i].x > sizeX - 20) {
                lights[i].x = sizeX - 20;
            }
            if (lights[i].y > sizeY - 20) {
                lights[i].y = sizeY - 20;
            }
        }
        //corner segments (x,y) = (0,0)
         Point(0, (float)sizeY);

        corners.push_back(Point(0,0));
        corners.push_back(Point((float)sizeX,0));
        corners.push_back(Point((float)sizeX,(float)sizeY));
        corners.push_back( Point(0, (float)sizeY));

        vertices.push_back(corners[0]);
        vertices.push_back(corners[1]);
        vertices.push_back(corners[2]);
        vertices.push_back(corners[3]);

        for(int i = 0; i < barriers.size(); i++)
        {
            for (int j = 0; j < barriers[i].point_count; j++)
            {
                vertices.push_back(Point(barriers[i].points[j].x, barriers[i].points[j].y));
                vertices.push_back(Point(barriers[i].points[j].x+math.epsilon,  barriers[i].points[j].y+math.epsilon));
                vertices.push_back(Point(barriers[i].points[j].x-math.epsilon,  barriers[i].points[j].y-math.epsilon));
            }
        }

        //draw logic here. find SDL library draw logic and put here.ctx.fillStyle = "#544";
        //for (i = 0; i < barriers.length; i++) {
          //  ctx.beginPath();
            //for (j = 0; j < barriers[i].point_count; j++) {
              //  ctx.lineTo(barriers[i].points[j].x_, barriers[i].points[j].y_);
            //}
            //ctx.fill();
        //}


        maxBoundry();
    }








};

class Entity : public Vector3D
{
    public:
        SDL_Rect rect;
        SDL_Event event;


    Entity(int x, int y, int w, int h) : Vector3D (x,y,1.0,1)
    {
        rect.x = x;
        rect.y = y;
        rect.w = w;
        rect.h = h;
    }
};


class Player : public Vector3D
{
    public:
        int speed;
        SDL_Rect rect;
        SDL_Event event;


    
    Player(int X, int Y, int W, int H, int s ): Vector3D (X,Y,1.0,1)
    {
        rect.x = X;
        rect.y = Y;
        rect.w = W;
        rect.h = H;
        
    }
    
    void move()
    {
        while ( SDL_PollEvent( &event ) )
        {
            if ( event.type == SDL_QUIT ){
                loop = false;
                
            }else if ( event.type == SDL_KEYDOWN )
            {
                switch ( event.key.keysym.sym )
                {
                    case SDLK_RIGHT:
                        rect.x += speed;
                        
                        break;
                    case SDLK_LEFT:
                        rect.x -=speed;
                        break;
                        // Remeber 0,0 in SDL is left-top. So when the user pressus down, the y need to increase
                    case SDLK_DOWN:
                        rect.y+= speed;
                        
                        break;
                    case SDLK_UP:
                        rect.y -= speed;
                        break;
                    default :
                        break;
                }
            }
        }
        
    }


    void draw()
    {
        SDL_SetRenderDrawColor( renderer, 0, 0, 255, 255 );
        SDL_RenderFillRect( renderer, &rect );
    }
};



Entity ent(100,100,55,55);
Player player(100,100, 50,50, 10);
std::vector< Entity > sprites;

int main( int argc, char* args[] )
{
    if ( !InitEverything() )
        return -1;
    RunGame();
}


void renderOtherSprites(std::vector<Entity> entities)
{
    SDL_SetRenderDrawColor( renderer, 255, 0, 0, 255 );
    for ( const auto &p : entities )
        SDL_RenderFillRect( renderer, &p.rect );
}


void RunGame()
{
    while ( loop ) //game loop
    {
        Render();
        player.move();
        SDL_Delay( 16 );// Add a 16msec delay to make our game run at ~60 fps
    }
}

void Render()
{

    SDL_RenderClear( renderer );
    player.draw();
    SDL_SetRenderDrawColor( renderer, 255, 255, 255, 255 );//screen color: white
    SDL_RenderPresent( renderer);
}
bool InitEverything()
{
    if ( !InitSDL() )
        return false;
    if ( !CreateWindow() )
        return false;
    if ( !CreateRenderer() )
        return false;
    SetupRenderer();
    return true;
}
bool InitSDL()
{
    if ( SDL_Init( SDL_INIT_EVERYTHING ) == -1 )
    {
        std::cout << " Failed to initialize SDL : " << SDL_GetError() << std::endl;
        return false;
    }
    
    return true;
}
bool CreateWindow()
{
    window = SDL_CreateWindow( "Game", posX, posY, sizeX, sizeY, 0 );
    if ( window == nullptr )
    {
        std::cout << "Failed to create window : " << SDL_GetError();
        return false;
    }
    return true;
}
bool CreateRenderer()
{
    renderer = SDL_CreateRenderer( window, -1, 0 );
    
    if ( renderer == nullptr )
    {
        std::cout << "Failed to create renderer : " << SDL_GetError();
        return false;
    }
    return true;
}
void SetupRenderer()
{
    // Set size of renderer to the same as window
    SDL_RenderSetLogicalSize( renderer, sizeX, sizeY );
    
    // Set color of renderer to red
    SDL_SetRenderDrawColor( renderer, 255, 0, 0, 255 );
}

bool CheckCollision( const SDL_Rect &rect1, const SDL_Rect &rect2 )
{
    // Find edges of rect1
    int left1 = rect1.x;
    int right1 = rect1.x + rect1.w;
    int top1 = rect1.y;
    int bottom1 = rect1.y + rect1.h;
    
    // Find edges of rect2
    int left2 = rect2.x;
    int right2 = rect2.x + rect2.w;
    int top2 = rect2.y;
    int bottom2 = rect2.y + rect2.h;
    
    // Check edges
    if ( left1 > right2 )// Left 1 is right of right 2
        return false; // No collision
    
    if ( right1 < left2 ) // Right 1 is left of left 2
        return false; // No collision
    
    if ( top1 > bottom2 ) // Top 1 is below bottom 2
        return false; // No collision
    
    if ( bottom1 < top2 ) // Bottom 1 is above top 2
        return false; // No collision
    
    return true;
}

/**
bool CheckEnemyCollisions()
{
    for ( const auto &p : enemies )
    {
        if ( CheckCollision( p.pos, playerPos) )
            return true;
    }
    
    return false;
}
 **/

/**
void ResetPlayerPos()
{
    // sizeX / 2 = middle pixel of the screen
    // playerPos.w / 2 = middle of the player
    // So setting player x pos to [middle of screen] - [middle of player] means it will be centerd in the screen.
    playerPos.x = ( sizeX / 2 ) - ( playerPos.w / 2 );
    playerPos.y = sizeY - bottomBar.h;
 
}
 **/

